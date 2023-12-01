import flet as ft

from flet_route import Routing, path
from views import *
from controllers import *
from model import  *

CREATE RouteManager(Routing):
    MODULE route_changed(self, route):
        pass
    
    MODULE change_route(self, route):
        CALL route_changed(route)
        super().change_route(route)
MODULE main(page: ft.Page):
	SET page.window_width = 1024
	SET page.window_height = 768
	SET page.title = "Morax"
if bool(page.client_storage.get("dark_mode")):
        SET page.theme_mode = ft.ThemeMode.DARK
    else:
        SET page.theme_mode = ft.ThemeMode.LIGHT
    
    SET colors = get_colors(page.client_storage.get("dark_mode"))
	
	SET confirm_email_page = ConfirmEmailPage()
	SET opening_page =  OpeningPage()
	SET signup_page = SignupPage()
	SET login_page =  LoginPage()
	SET forgot_password_page = ForgotPasswordPage()
	SET onboarding_page =  OnboardingPage()
	SET home_page = call HomePage()
	
	SET main_pages = [confirm_email_page, opening_page, signup_page, login_page, forgot_password_page, onboarding_page, 		home_page]

    SET app_routes = [
       	 path(url="/", clear=True, view=opening_page.get_view),
       	 path(url="/login", clear=True, view=login_page.get_view),
         path(url="/signup", clear=True, view=signup_page.get_view), 
         path(url="/forgot_password", clear=True, view=forgot_password_page.get_view),
         path(url="/confirm_email", clear=True, view=confirm_email_page.get_view),
         path(url="/home", clear=True, view=home_page.get_view),
         path(url="/onboarding", clear=False, view=onboarding_page.get_view)
    ]
    
    	CALL Routing(page = page, app_routes = app_routes)
   	CALL page.go(page.route)
	MODULE handle_route_changed(event: ft.RouteChangeEvent):
       	 for current in main_pages:
            if current.route_address == event.route:
                current.update_colors(colors)
                break

    	CALL routing.route_changed = handle_route_changed
    
    	CALL opening_page.update_colors(colors)

   	CALL opening_page.update()
    

    
 
    if page.client_storage.get("currency") is None:
        SET page.client_storage TO ("currency", "PHP")
    if page.client_storage.get("dark_mode") is None:
        SET page.client_storage TO ("dark_mode", "False")
    
    SET model =  Model()

   	Call HomeController(page, model, home_page)
    	Call AddDialogController(page, model, home_page)
    	Call ItemInfoDialogController(page, model, home_page)
    	Call AddReceivableDialogController(page, model, home_page)
    	Call AccountSettingsDialogsController(page, model, home_page)
    	Call ReceivableInfoDialogController(page, model, home_page)
    	Call OpeningController(page, model, opening_page)
    	Call OnboardingController(page, model, onboarding_page)
   	Call LoginController(page, model, login_page)
    	Call SignupController(page, model, signup_page)
    	Call ForgotController(page, model, forgot_password_page)
    	Call ConfirmEmailController(page, model, confirm_email_page)

if __name__ == "__main__":
    Call  ft.app(
        target=main,
        assets_dir="assets"
    )


