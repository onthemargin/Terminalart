from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, ListItem, ListView, Static, Label
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.binding import Binding

from generators.registry import GeneratorRegistry


class AsciiArtApp(App):
    """ASCII Art Gallery Application."""

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("escape", "quit", "Quit"),
    ]

    CSS = """
    Horizontal {
        height: 100%;
    }

    #menu-container {
        width: 30;
        border-right: solid $primary;
    }

    #menu-list {
        height: 100%;
    }

    #canvas-container {
        width: 1fr;
        align: center middle;
    }

    #ascii-art {
        width: auto;
        height: auto;
        text-align: center;
    }

    ListView {
        background: $surface;
    }

    ListItem {
        padding: 1 2;
    }

    ListItem:hover {
        background: $boost;
    }
    """

    def __init__(self):
        super().__init__()
        self.registry = GeneratorRegistry()
        self.current_art = None

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            with Vertical(id="menu-container"):
                yield ListView(
                    *[ListItem(Label(f"🎨 {gen.name}")) for gen in self.registry.get_all()],
                    id="menu-list"
                )
            with VerticalScroll(id="canvas-container"):
                yield Static("Select an object from the menu", markup=True, id="ascii-art")
        yield Footer()

    def on_mount(self) -> None:
        self.title = "Terminal Art"
        self.sub_title = "Select an object to view"
        # Show the first item by default
        generators = self.registry.get_all()
        if generators:
            ascii_widget = self.query_one("#ascii-art", Static)
            ascii_widget.update(generators[0].generate())

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Handle selection from the menu."""
        selected_index = event.list_view.index
        generators = self.registry.get_all()
        if selected_index is not None and selected_index < len(generators):
            selected_gen = generators[selected_index]
            ascii_widget = self.query_one("#ascii-art", Static)
            ascii_widget.update(selected_gen.generate())

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        """Update canvas as user navigates with arrow keys."""
        if event.item is not None:
            selected_index = event.list_view.index
            generators = self.registry.get_all()
            if selected_index is not None and selected_index < len(generators):
                selected_gen = generators[selected_index]
                ascii_widget = self.query_one("#ascii-art", Static)
                ascii_widget.update(selected_gen.generate())


def main():
    """Entry point for the application."""
    app = AsciiArtApp()
    app.run()


if __name__ == "__main__":
    main()
