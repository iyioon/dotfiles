# Dotfiles

Zsh configuration with Oh My Zsh, Powerlevel10k, and productivity plugins.

Themed to match my Neovim config: [iyioon/nvim](https://github.com/iyioon/nvim) (cyberdream colorscheme).

## Color Scheme

| Color | Hex | Used For |
|-------|-----|----------|
| ![Blue](https://img.shields.io/badge/Blue-5ea1ff?style=flat-square) | `#5ea1ff` | Directory, time, environment |
| ![Green](https://img.shields.io/badge/Green-5eff6c?style=flat-square) | `#5eff6c` | Valid commands, git branch |
| ![Magenta](https://img.shields.io/badge/Magenta-ff5ef1?style=flat-square) | `#ff5ef1` | Prompt symbol, frame |
| ![Red](https://img.shields.io/badge/Red-ff6e5e?style=flat-square) | `#ff6e5e` | Invalid commands, errors |
| ![Grey](https://img.shields.io/badge/Grey-7b8496?style=flat-square) | `#7b8496` | Autosuggestions |

## Installation

### 1. Clone this repo
```bash
git clone https://github.com/iyioon/dotfiles.git ~/dotfiles
```

### 2. Install dependencies

**macOS / Linux with Homebrew:**
```bash
brew install zsh fzf zoxide atuin
```

**Linux (apt):**
```bash
sudo apt install zsh fzf
curl -sSfL https://raw.githubusercontent.com/ajeetdsouza/zoxide/main/install.sh | sh
curl --proto '=https' --tlsv1.2 -LsSf https://setup.atuin.sh | sh
```

### 3. Install Oh My Zsh
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### 4. Install Powerlevel10k theme
```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \
  ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

### 5. Install Zsh plugins
```bash
git clone https://github.com/zsh-users/zsh-autosuggestions \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

git clone https://github.com/zsh-users/zsh-syntax-highlighting \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

### 6. Set up fzf key bindings
```bash
$(brew --prefix)/opt/fzf/install
```

### 7. Link the configs
```bash
ln -sf ~/dotfiles/.zshrc ~/.zshrc
ln -sf ~/dotfiles/.p10k.zsh ~/.p10k.zsh
source ~/.zshrc
```

To customize the prompt yourself, run `p10k configure`.

## Plugin Usage

| Plugin | What it does | Usage |
|--------|--------------|-------|
| **git** | Git aliases and completions | `gst` (status), `gco` (checkout), `gp` (push) |
| **web-search** | Search from terminal | `google query`, `ddg query`, `youtube query` |
| **zsh-autosuggestions** | Fish-like suggestions | Type, then `→` to accept |
| **zsh-syntax-highlighting** | Command coloring | Valid commands = green, errors = red |
| **fzf** | Fuzzy finder | `Ctrl-R` history, `Ctrl-T` files, `Alt-C` cd |
| **zoxide** | Smart directory jumper | `cd foo` jumps to most-used match |
| **atuin** | Enhanced history | `Ctrl-R` for searchable history with context |
