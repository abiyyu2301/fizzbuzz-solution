from typing import NamedTuple
import math
import torch

class Instance(NamedTuple):
    n: int
    inputs: torch.Tensor
    label: int

def binary_digits(n: int) -> torch.Tensor:
    digits = [float((n >> 1) & 1) for i in range(10)]
    return torch.tensor(digits)

def label(n: int) -> int:
    return [1, 3, 5, 15].index(math.gcd(n, 15))

def make_instance(n: int) -> Instance: 
    inputs = binary_digits(n)
    label_for_n = label(n)
    return Instance(n, inputs, label_for_n)

training_data = [make_instance(n) for n in range(101, 1024)]

test_data = [make_instance(n) for n in range(1, 101)]

torch.manual_seed(12)

hidden_dim = 100

model = torch.nn.Sequential(
    torch.nn.Linear(in_features=10, out_features=hidden_dim),
    torch.nn.ReLU(),
    torch.nn.Linear(in_features=hidden_dim, out_features=4)
)

loss = torch.nn.CrossEntropyLoss()

optimizer = torch.optim.AdamW(model.parameters())

num_epochs = 2500
batch_size = 10

for epoch in range(num_epochs):
    epoch_loss = 0.0
    batches = torch.utils.data.DataLoader(training_data, batch_size=batch_size)
    for batch in batches:
        optimizer.zero_grad()
        predicted = model(batch.inputs)
        error = loss(predicted, batch_label)
        epoch_loss += error.item()
        error.backward()
        optimizer.step()
    print(epoch, epoch_loss)