<!-- living-code-readme:1 -->
# 🔓 Living Code for OpenCode

**Calm slate. Living color.** Living Code for OpenCode TUI: complete native JSON palettes for UI, Markdown, syntax highlighting, selections and review diffs.

[Installation](#installation) · [Flavors](#flavors) · [Configuration](#configuration) · [All ports](https://github.com/living-code-theme)

## Previews

Real application screenshots have not been captured yet.

## Installation

```sh
git clone https://github.com/living-code-theme/opencode.git
cd opencode
```

```sh
mkdir -p "${XDG_CONFIG_HOME:-$HOME/.config}/opencode/themes"
cp themes/*.json "${XDG_CONFIG_HOME:-$HOME/.config}/opencode/themes/"
```

Restart OpenCode and run `/theme`, then choose `living-code-night`. For project-only installation, copy the files into `.opencode/themes/` instead.

## Flavors

Expand a flavor for its full-size preview and activation instructions.

<details data-lc-flavor="night">
<summary><strong>Night</strong> · Dark · full palette</summary>

A real application capture is not available yet.

Choose `living-code-night` with `/theme`, or set `"theme": "living-code-night"` in your existing `tui.json`.

</details>

<details data-lc-flavor="frost">
<summary><strong>Frost</strong> · Dark · softer chroma</summary>

A real application capture is not available yet.

Choose `living-code-frost` with `/theme`, or set `"theme": "living-code-frost"` in your existing `tui.json`.

</details>

<details data-lc-flavor="paper">
<summary><strong>Paper</strong> · Light · near-white slate</summary>

A real application capture is not available yet.

Choose `living-code-paper` with `/theme`, or set `"theme": "living-code-paper"` in your existing `tui.json`.

</details>

<details data-lc-flavor="signal">
<summary><strong>Signal</strong> · Dark · teal accent</summary>

A real application capture is not available yet.

Choose `living-code-signal` with `/theme`, or set `"theme": "living-code-signal"` in your existing `tui.json`.

</details>

## Configuration

The files use the OpenCode v1 `{ "theme": { … } }` JSON format. They provide every required color, explicit selected-item text and menu backgrounds. Every flavor is a separate theme, so Paper stays light even in a dark terminal. Put configuration in `tui.json`, not in the theme file; preserve any existing keybindings.

## Compatibility

Targets the TUI theme format verified against OpenCode 1.19.0. This is not the web/desktop theme format. Truecolor gives the intended colors; reduced-color terminals approximate them. OpenCode 2 theme documents are a different API and are not claimed here. Syntax, Markdown and diff color contracts are checked independently of generation.

## Contributing

Found a problem? [Open an issue](https://github.com/living-code-theme/opencode/issues/new/choose) with the app version, the flavor and a screenshot. Want Living Code somewhere else? [Request a port](https://github.com/living-code-theme/core/issues/new?template=port-request.yml).

Pull requests are welcome. Keep this README, `port.json` and `images/` in sync, and use real screenshots of the app, never mockups.

🦎 **One chameleon, many habitats.** Part of [Living Code](https://github.com/living-code-theme).

## License

[MIT](LICENSE) © Elliot Luque
