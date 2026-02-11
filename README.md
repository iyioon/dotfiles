# Dotfiles

Zsh configuration with Oh My Zsh, Powerlevel10k, and productivity plugins.

## Installation

### 1. Install dependencies

**macOS:**
```bash
brew install zsh fzf zoxide atuin
```

**Linux (Debian/Ubuntu):**
```bash
sudo apt install zsh fzf
curl -sSfL https://raw.githubusercontent.com/ajeetdsouza/zoxide/main/install.sh | sh
curl --proto '=https' --tlsv1.2 -LsSf https://setup.atuin.sh | sh
```

### 2. Install Oh My Zsh
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### 3. Install Powerlevel10k theme
```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \
  ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

### 4. Install Zsh plugins
```bash
git clone https://github.com/zsh-users/zsh-autosuggestions \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

git clone https://github.com/zsh-users/zsh-syntax-highlighting \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

### 5. Set up fzf key bindings
```bash
# macOS
$(brew --prefix)/opt/fzf/install

# Linux (if installed via apt)
# Key bindings are usually auto-configured
```

### 6. Apply the config
```bash
cp .zshrc ~/.zshrc
source ~/.zshrc
```

Run `p10k configure` to set up your prompt.

## Plugin Usage

| Plugin | What it does | Usage |
|--------|--------------|-------|
| **git** | Git aliases and completions | `gst` (status), `gco` (checkout), `gp` (push) |
| **web-search** | Search from terminal | `google foo`, `ddg bar` |
| **zsh-autosuggestions** | Fish-like suggestions | Type, then `→` to accept |
| **zsh-syntax-highlighting** | Command coloring | Valid commands = green, errors = red |
| **fzf** | Fuzzy finder | `Ctrl-R` history, `Ctrl-T` files, `Alt-C` cd |
| **zoxide** | Smart directory jumper | `cd foo` jumps to most-used match |
| **atuin** | Enhanced history | `Ctrl-R` for searchable history with context |
