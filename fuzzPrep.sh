#!/bin/bash

# Install Slither and its dependencies
echo "Installing solc and slither..."
sudo apt install python3.10-venv
sudo apt install python3-pip
python3 -m venv ~/venv
source ~/venv/bin/activate
pip3 install solc-select slither-analyzer crytic-compile
solc-select install 0.8.25
solc-select use 0.8.25

# Install Echidna
if ! command -v echidna >/dev/null 2>&1; then
    echo "Installing echidna..."
    curl -Lo /tmp/echidna.tar.gz \
        https://github.com/crytic/echidna/releases/download/v2.2.6/echidna-2.2.6-x86_64-linux.tar.gz
    tar -xzf /tmp/echidna.tar.gz -C /tmp
    sudo mv /tmp/echidna /usr/local/bin
    rm /tmp/echidna.tar.gz
fi

# Install Foundry
if ! command -v forge >/dev/null 2>&1; then
    echo "Installing Foundry..."
    curl -L https://foundry.paradigm.xyz | bash

    # Add Foundry to PATH and make it persistent
    export PATH="$HOME/.foundry/bin:$PATH"
    echo 'export PATH="$HOME/.foundry/bin:$PATH"' >> ~/.bashrc

    # Initialize Foundry
    $HOME/.foundry/bin/foundryup

    # Verify installation
    echo "=== Verifying Foundry Installation ==="
    $HOME/.foundry/bin/forge --version
fi

# Source bashrc to apply all PATH changes
source ~/.bashrc

export PATH="/root/venv/bin:/.foundry/bin:$PATH"
echo $PATH