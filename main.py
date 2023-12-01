START
IMPORT flet AS ft

FROM flet_route IMPORT Routing, path
FROM views IMPORT *
FROM controllers IMPORT *
FROM models IMPORT  *
FROM repository IMPORT *

CREATE RouteManager(Routing)
    MODULE route_changed(self, route)
        pass
    
    MODULE change_route(self, route)
        CALL route_changed(route)
        SUPER().change_route(route)

MODULE main(page: ft.Page)
	SET page.window_width = 1024
	SET page.window_height = 768
	SET page.title = "Morax"

    IF bool(page.client_storage.get("dark_mode")) THEN
        SET page.theme_mode = ft.ThemeMode.DARK
    ELSE
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

    CREATE LIST app_routes = [
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
	MODULE handle_route_changed(event: ft.RouteChangeEvent)
       	 FOR current in main_pages
            IF current.route_address == event.route THEN
                current.update_colors(colors)
                BREAK

    	CALL routing.route_changed = handle_route_changed
    
    	CALL opening_page.update_colors(colors)

   	CALL opening_page.update()
    

    
 
    IF page.client_storage.get("currency") is None THEN
        SET page.client_storage TO ("currency", "PHP")
    IF page.client_storage.get("dark_mode") is None THEN
        SET page.client_storage TO ("dark_mode", "False")
    
    SET model =  Model()

   	CALL HomeController(page, model, home_page)
    	CALL AddDialogController(page, model, home_page)
    	CALL ItemInfoDialogController(page, model, home_page)
    	CALL AddReceivableDialogController(page, model, home_page)
    	CALL AccountSettingsDialogsController(page, model, home_page)
    	CALL ReceivableInfoDialogController(page, model, home_page)
    	CALL OpeningController(page, model, opening_page)
    	CALL OnboardingController(page, model, onboarding_page)
   	CALL LoginController(page, model, login_page)
    	CALL SignupController(page, model, signup_page)
    	CALL ForgotController(page, model, forgot_password_page)
    	CALL ConfirmEmailController(page, model, confirm_email_page)

IF __name__ == "__main__" THEN
    CALL  ft.app(
        target=main,
        assets_dir="assets"
    )

END
