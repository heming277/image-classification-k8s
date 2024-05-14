import numpy as np
import torchvision
import torchvision.transforms as transforms
from sklearn.model_selection import train_test_split
from torch.utils.data import Subset
import torch

def preprocess_data():
    # Define transformations
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    # Load the dataset
    dataset = torchvision.datasets.CIFAR10(root='~/datasets/cifar-10', train=True, download=True, transform=transform)

    # Split dataset into train and validation sets
    train_idx, val_idx = train_test_split(list(range(len(dataset))), test_size=0.2, random_state=42)

    # Create data subsets for train and validation
    train_data = Subset(dataset, train_idx)
    val_data = Subset(dataset, val_idx)

    # Create data loaders
    trainloader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)
    valloader = torch.utils.data.DataLoader(val_data, batch_size=64, shuffle=False)

    # Save the indices of train and validation sets (optional)
    np.save('train_indices.npy', train_idx)
    np.save('val_indices.npy', val_idx)

    return trainloader, valloader

# Uncomment the following line to preprocess data when this script is run directly
# trainloader, valloader = preprocess_data()