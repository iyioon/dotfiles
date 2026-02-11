# Dotfiles

Zsh configuration with Oh My Zsh, Powerlevel10k, and productivity plugins.

Themed to match my Neovim config: [iyioon/nvim](https://github.com/iyioon/nvim) (cyberdream colorscheme).

## Color Scheme

| Color | Hex | Used For |
|-------|-----|----------|
| ![#5ea1ff](https://via.placeholder.com/12/5ea1ff/5ea1ff.png) Blue | `#5ea1ff` | Directory, time, environment |
| ![#5eff6c](https://via.placeholder.com/12/5eff6c/5eff6c.png) Green | `#5eff6c` | Valid commands, git branch |
| ![#ff5ef1](https://via.placeholder.com/12/ff5ef1/ff5ef1.png) Magenta | `#ff5ef1` | Prompt symbol, frame |
| ![#ff6e5e](https://via.placeholder.com/12/ff6e5e/ff6e5e.png) Red | `#ff6e5e` | Invalid commands, errors |
| ![#7b8496](https://via.placeholder.com/12/7b8496/7b8496.png) Grey | `#7b8496` | Autosuggestions |

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
