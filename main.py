import flet as ft


def input_field(width, height, hint_text, icon, password=False):
    return ft.Container(
        border=ft.border.all(1,"#44f4f4f4"),
        border_radius=18,
        bgcolor="transparent",
        margin=ft.margin.only(top=20,bottom=20,left=60,right=60),
        padding=10,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.TextField(
                    width=width,
                    height=height,
                    hint_text=hint_text,
                    hover_color=ft.colors.TRANSPARENT,
                    border=ft.InputBorder.NONE,
                    border_radius=18,
                    color='white',
                    hint_style=ft.TextStyle(
                        color="white"
                    ),
                    bgcolor="transparent",
                    text_style=ft.TextStyle(
                        size=18,
                        weight="w400"
                    ),
                    password=password
                ),
                ft.Container(
                    margin=ft.margin.only(left=10),
                    content=ft.Icon(
                        icon,
                        color="white",
                    )
                )
            ]
        )
    )



def body(page:ft.Page):
    return ft.Container(
        alignment=ft.alignment.center,
        content = ft.Stack(
            controls=[
                ft.Image(
                    "assets/bgpic.jpg"
                ),         
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Container(
                        width=500,
                        height=500,
                        margin=ft.margin.only(top='100'),
                        border_radius=18,
                        border=ft.border.all(1, "#44fafafa"),
                        blur=ft.Blur(10,12, ft.BlurTileMode.MIRROR),
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            "Login",
                                            color="white",
                                            weight="w600",
                                            size=24,
                                            text_align="center",
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                ft.Row(
                                    controls=[
                                        input_field(
                                            width=320,
                                            height=60,
                                            hint_text="username",
                                            icon=ft.icons.PERSON_2_ROUNDED
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                ft.Row(
                                    controls=[
                                        input_field(
                                            width=320,
                                            height=60,
                                            hint_text="password",
                                            icon=ft.icons.LOCK_ROUNDED,
                                            password=True
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                            width=370,
                                            content=ft.Row(
                                                controls=[
                                                    ft.Row(
                                                        controls=[
                                                            ft.Checkbox(
                                                                value=False, 
                                                                hover_color=ft.colors.TRANSPARENT,
                                                            ),
                                                            ft.Text(
                                                                "Remember me", 
                                                                color="white", 
                                                                size=12,
                                                            )
                                                        ],
                                                        spacing=0
                                                    ),
                                                    ft.Text(
                                                        "Forgot password?",
                                                        color="white",
                                                        size=14
                                                    )
                                                ],
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                            )
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                ft.Row(
                                    controls=[
                                        ft.ElevatedButton(
                                            "Login",
                                            color="black",
                                            bgcolor="white",
                                            width=320,
                                            height=50
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            "Don't have a account?",
                                            color="white",
                                            size=14
                                        ),
                                        ft.Text(
                                            "Register",
                                            weight="w500",
                                            color="white",
                                            size=14
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=3
                                )
                            ]
                        )
                    ),
                ),
                ft.Row(
                    [
                        ft.WindowDragArea(
                            ft.Container(
                                bgcolor=ft.colors.TRANSPARENT, padding=10,
                                content=ft.Row(
                                    controls=[
                                        ft.Container(),
                                        ft.Row(
                                            controls=[
                                                ft.IconButton(
                                                    ft.icons.CLOSE, 
                                                    on_click=lambda _: page.window_close(),
                                                    icon_color="white",
                                                    hover_color=ft.colors.WHITE10
                                                )
                                            ]
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                )
                            ), 
                            expand=True
                        )
                    ]
                )
            
            ]
        )
    )


def main(page: ft.Page):


    page.window_title_bar_hidden = True
    page.window_frameless = True
    page.window_resizable = False
    
    page.padding = 0
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    page.add(body(page))






if __name__ == "__main__":
    
    ft.app(target=main, view=ft.AppView.FLET_APP_HIDDEN)
