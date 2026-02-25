# Dotfiles

Zsh configuration with Oh My Zsh, Powerlevel10k, and productivity plugins.

Themed to match my Neovim config: [iyioon/nvim](https://github.com/iyioon/nvim) (cyberdream colorscheme).

## Color Scheme

| Color | Hex | Used For |
|-------|-----|----------|
| ![Magenta](https://img.shields.io/badge/Magenta-ff5ef1?style=flat-square) | `#ff5ef1` | Directory, time, environment, prompt symbol |
| ![Cyan](https://img.shields.io/badge/Cyan-5ef1ff?style=flat-square) | `#5ef1ff` | SSH context |
| ![Green](https://img.shields.io/badge/Green-5eff6c?style=flat-square) | `#5eff6c` | Valid commands, git branch |
| ![Red](https://img.shields.io/badge/Red-ff6e5e?style=flat-square) | `#ff6e5e` | Invalid commands, errors, root |
| ![Grey](https://img.shields.io/badge/Grey-7b8496?style=flat-square) | `#7b8496` | Autosuggestions, frame lines |

## Installation

### 1. Clone this repo
```bash
git clone https://github.com/iyioon/dotfiles.git ~/dotfiles
```

### 2. Install Homebrew (if not installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 3. Install dependencies

```bash
brew install zsh fzf zoxide atuin navi
```

### 4. Install Oh My Zsh
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### 5. Install Powerlevel10k theme
```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \
  ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

### 6. Install Zsh plugins
```bash
git clone https://github.com/zsh-users/zsh-autosuggestions \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

git clone https://github.com/zsh-users/zsh-syntax-highlighting \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

### 7. Set up fzf key bindings
```bash
$(brew --prefix)/opt/fzf/install
```

### 8. Link the configs
```bash
ln -sf ~/dotfiles/.zshrc ~/.zshrc
ln -sf ~/dotfiles/.p10k.zsh ~/.p10k.zsh
mkdir -p ~/.config/navi
ln -sf ~/dotfiles/navi/config.yaml ~/.config/navi/config.yaml
ln -sf ~/dotfiles/navi/cheats ~/.config/navi/cheats
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
| **fzf** | Fuzzy finder | `Ctrl-T` files, `Alt-C` cd |
| **zoxide** | Smart directory jumper | `cd foo` jumps to most-used match |
| **atuin** | Enhanced history | `Ctrl-R` searchable history with context, filters, optional sync |
| **navi** | Interactive cheatsheet | `Ctrl-G` command palette for browsing and executing commands |

## Navi Cheatsheets

Custom cheatsheets are stored in `navi/cheats/`. To add community cheatsheets:

```bash
navi repo add denisidoro/cheats
```

## Optional: Set Zsh as Default Shell

If you can change your default shell:
```bash
chsh -s $(which zsh)
```

If the server doesn't allow changing the default shell, add this to `~/.bashrc` to auto-launch zsh:
```bash
echo 'if [ -t 1 ] && command -v zsh >/dev/null 2>&1 && [ -z "$ZSH_VERSION" ]; then exec zsh -l; fi' >> ~/.bashrc
```
