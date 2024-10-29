from tqdm import tqdm
import torch
from torch.utils.data import DataLoader, Dataset
from torch.nn import init
from torch import nn, optim
from functools import partial
import matplotlib.pyplot as plt

def get_conv_model(in_ch=1):
    """
    Create and return a convolutional neural network model with the given number of input channels.

    The weights of the convolutional and linear layers are initialized using Kaiming normal initialization.

    Parameters:
    - in_ch (int, optional): The number of input channels to the network. Default is 1.

    Returns:
    - nn.Sequential: The constructed convolutional neural network model.
    
    Structure:
    - Input: [in_ch x 28 x 28]
    - Conv1 -> BatchNorm -> ReLU: [4 x 14 x 14]
    - Conv2 -> BatchNorm -> ReLU: [8 x 7 x 7]
    - Conv3 -> BatchNorm -> ReLU: [16 x 4 x 4]
    - Conv4 -> BatchNorm -> ReLU -> AdaptiveAvgPool -> Flatten: [32]
    - Linear: [10]
    """
    conv_model =  nn.Sequential(
    # 1x28x28
    nn.Conv2d(in_ch, 4, kernel_size=3, stride=2, padding=1),
    nn.BatchNorm2d(4),
    nn.ReLU(),
    # 4x14x14
    nn.Conv2d(4, 8, kernel_size=3, stride=2, padding=1),
    nn.BatchNorm2d(8),
    nn.ReLU(),
    # 8x7x7
    nn.Conv2d(8, 16, kernel_size=3, stride=2, padding=1),
    nn.BatchNorm2d(16),
    nn.ReLU(),
    # 16x4x4
    nn.Conv2d(16, 32, kernel_size=3, stride=2, padding=1),
    nn.BatchNorm2d(32),
    nn.ReLU(),
    # 32x2x2 -> GAP -> 32 x 1 x 1
    nn.AdaptiveAvgPool2d(1),
    nn.Flatten(),
    nn.Linear(32, 10)
    # 10
    )
    for layer in conv_model:
        if isinstance(layer, nn.Linear) or isinstance(layer, nn.Conv2d):
            init.kaiming_normal_(layer.weight)
    return conv_model

def learn(model, train_loader, val_loader, optimizer, loss_func, num_epoch, early_stopping=None, save_path=None, scheduler=None):
    """
    Train and validate a given PyTorch model.
    
    Parameters:
    - model: PyTorch model to train. Model needs to be on GPU beforehand if it's supposed to be trained on GPU.
    - train_loader: DataLoader for training data.
    - val_loader: DataLoader for validation data.
    - optimizer: PyTorch optimizer.
    - loss_func: PyTorch loss function.
    - num_epoch: Number of epochs for training.
    - early_stopping: Number of epochs with no improvement to stop training. None means no early stopping.
    - save_path: Path to save the best model.
    - scheduler: Learning rate scheduler. None means no scheduler.
    
    Returns:
    - train_losses: List of training losses.
    - val_losses: List of validation losses.
    - val_accuracies: List of validation accuracies.
    """
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu") 
    # ログ
    train_losses = []
    val_losses = []
    val_accuracies = []
    
    best_val_loss = float('inf')
    no_improve = 0 # カウント用変数
    
    for epoch in range(num_epoch):
        model.train()
        running_loss = 0.0
        running_val_loss = 0.0
        running_val_acc = 0.0
        
        for train_batch, data in tqdm(enumerate(train_loader), total=len(train_loader), desc="Training", leave=False):
            
            X, y = data
            X, y = X.to(device), y.to(device)
            optimizer.zero_grad()
            # forward
            preds = model(X)
            loss = loss_func(preds, y)
            running_loss += loss.item()
    
            # backward
            loss.backward()
            optimizer.step()
            
        model.eval()
        # validation
        with torch.no_grad():
            for val_batch, data in tqdm(enumerate(val_loader), total=len(val_loader), desc="Validation", leave=False):
                X_val, y_val = data
                X_val, y_val = X_val.to(device), y_val.to(device)
                preds_val = model(X_val)
                val_loss = loss_func(preds_val, y_val)
                running_val_loss += val_loss.item()
                val_accuracy = torch.sum(torch.argmax(preds_val, dim=-1) == y_val) / y_val.shape[0]
                running_val_acc += val_accuracy.item()
    
        train_losses.append(running_loss/(train_batch + 1))
        val_losses.append(running_val_loss/(val_batch + 1))
        val_accuracies.append(running_val_acc/(val_batch + 1))
        print(f'epoch: {epoch}: train error: {train_losses[-1]}, validation error: {val_losses[-1]}, validation accuracy: {val_accuracies[-1]}')
    
        if val_losses[-1] < best_val_loss:
            best_val_loss = val_losses[-1]
            no_improve = 0
            if save_path is not None:
                state = {
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'val_loss': val_losses[-1]
                }
                torch.save(state, save_path)
        else:
            no_improve += 1
    
        if early_stopping and no_improve >= early_stopping:
            print('Stopping early')
            break
        if scheduler:
            scheduler.step()

    return train_losses, val_losses, val_accuracies

class ActivationStatistics:
    """
    A utility class for gathering statistics on activations produced by ReLU layers in a model.

    Attributes:
    - model (nn.Module): The model whose activations are to be tracked.
    - act_means (List[List[float]]): List of means for each ReLU layer's activations.
    - act_stds (List[List[float]]): List of standard deviations for each ReLU layer's activations.

    Methods:
    - register_hook: Register hooks on ReLU layers of the model to gather statistics.
    - save_out_stats: Callback method to save statistics of activations.
    - get_statistics: Return collected activation means and standard deviations.
    - plot_statistics: Plot the activation statistics using matplotlib.

    Usage:
        model = ... # some PyTorch model
        act_stats = ActivationStatistics(model)
        ... # Run the model, gather statistics
        act_stats.plot_statistics()
    """
    def __init__(self, model):
        self.model = model
        self.act_means = [[] for module in self.model if isinstance(module, nn.ReLU)]
        self.act_stds = [[] for module in self.model if isinstance(module, nn.ReLU)]
        self.register_hook()

    def register_hook(self):
        relu_layers = [module for module in self.model if isinstance(module, nn.ReLU)]
        for i, relu in enumerate(relu_layers):
            relu.register_forward_hook(partial(self.save_out_stats, i))

    def save_out_stats(self, i, module, inp, out):
        self.act_means[i].append(out.detach().cpu().mean().item())
        self.act_stds[i].append(out.detach().cpu().std().item())

    def get_statistics(self):
        return self.act_means, self.act_stds

    def plot_statistics(self):
        fig, axs = plt.subplots(1, 2, figsize=(15, 5))
        for act_mean in self.act_means:
            axs[0].plot(act_mean)
        axs[0].set_title('Activation means')
        axs[0].legend(range(len(self.act_means)))

        for act_std in self.act_stds:
            axs[1].plot(act_std)
        axs[1].set_title('Activation stds')
        axs[1].legend(range(len(self.act_stds)))

        plt.show()
        

def lr_finder(model, train_loader, loss_func, lr_multiplier=1.2):
    """
    Find an optimal learning rate using the learning rate range test.
    
    Parameters:
    - model: PyTorch model.
    - train_loader: DataLoader for training data.
    - loss_func: PyTorch loss function.
    - lr_multiplier: Multiplier to increase the learning rate at each step.
    
    Returns:
    - lrs: List of tested learning rates.
    - losses: List of losses corresponding to the learning rates.
    """
    lr = 1e-8
    max_lr = 10
    opt = torch.optim.SGD(model.parameters(), lr=lr)
    losses = []
    lrs = []

    for train_batch, data in enumerate(train_loader):
        X, y = data
        
        opt.zero_grad()
        # forward
        preds = model(X)
        loss = loss_func(preds, y)
        losses.append(loss.item())
        lrs.append(lr)

        # backward
        loss.backward()
        opt.step()

        lr *= lr_multiplier

        for param_group in opt.param_groups:
            param_group['lr'] = lr
        if lr > max_lr:
            break

    return lrs, losses