import flet as ft
import time

def main(page: ft.Page):
    page.title = "Flet WebView App"
    page.padding = 0

    # Splash screen
    splash_screen = ft.Column(
        [
            ft.ProgressRing(),
            ft.Text("Loading..."),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )
    page.add(splash_screen)
    page.update()
    time.sleep(2)

    # Main content
    loading_bar = ft.ProgressBar(visible=False)

    # Load last URL or use default
    initial_url = page.client_storage.get("last_url") or "https://flet.dev"

    webview = ft.WebView(
        initial_url,
        expand=True,
        on_page_started=lambda e: show_loading_bar(True),
        on_page_ended=lambda e: show_loading_bar(False),
    )

    def show_loading_bar(show):
        loading_bar.visible = show
        page.update()

    def change_site(e):
        def close_dialog(e):
            url = url_input.value
            if url:
                webview.url = url
                webview.update()
                page.client_storage.set("last_url", url)  # Save the new URL
            page.dialog.open = False
            page.update()

        url_input = ft.TextField(label="Enter URL", value=webview.url)
        page.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Change Site"),
            content=url_input,
            actions=[
                ft.TextButton("Go", on_click=close_dialog),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.dialog.open = True
        page.update()

    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.NavigationDrawerDestination(
                icon=ft.icons.WEB,
                label="Change Site",
            ),
        ],
        on_change=lambda e: change_site(e) if e.control.selected_index == 0 else None
    )

    def open_drawer(e):
        page.drawer.open = True
        page.drawer.update()

    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.icons.MENU, on_click=open_drawer),
        title=ft.Text("Flet WebView App"),
        actions=[loading_bar],
    )

    main_content = ft.Column([webview], expand=True)

    # Hide splash screen and show main content
    splash_screen.visible = False
    page.add(main_content)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
