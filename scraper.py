from playwright.sync_api import sync_playwright

CANVAS_URL = "https://www.umass.edu/it/canvas"
import getpass

def login_canvas():
    username = input("Enter your UMass username: ")
    password = getpass.getpass("Enter your Canvas password: ")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        
        try:
            # OPEN UMASS CANVAS
            page.goto(CANVAS_URL)
            print("✅ Opened Canvas successfully")
            
            # CLICK LOG INTO CANVAS
            page.wait_for_selector("text=LOG INTO CANVAS",timeout = 10000)
            page.click("text=LOG INTO CANVAS")
            page.wait_for_load_state("Loading...")

            # FILL USERNAME AND PASSWORD
            page.wait_for_selector("#username", timeout=15000)
            print("loading...")
            
            page.wait_for_url("https://login.microsoftonline.com/*", timeout = 20000)
            page.wait_for_selector("input[type = 'email']", timeout = 15000)
            
            page.fill("input[type = 'email']", username)
            page.click("text = NEXT")
            print("Moving to password")
            
            page.wait_for_selector("input[type = 'password']", timeout = 15000)
            
            page.fill("input[type='password']", password)
            page.click("input[type='submit']")
            print("Logging in...")
            
            # Handle Microsoft 2FA/second login step
            page.wait_for_url("https://login.microsoftonline.com/*", timeout=20000)
            
            # Check if we need to verify the account
            if page.locator("text=Verify your identity").is_visible():
                print("Additional verification required...")
                
                # Click "Sign in with Microsoft Authenticator" if present
                if page.locator("text=Sign in with Microsoft Authenticator").is_visible():
                    page.click("text=Sign in with Microsoft Authenticator")
                
                print("Please approve the login request on your Microsoft Authenticator app")
                input("Press Enter after you've approved the request...")
            
            # Wait for successful login and redirect to Canvas
            page.wait_for_url("*canvas*", timeout=60000)
            page.wait_for_load_state("domcontentloaded")
            
            print("Logged in successfully, current page is", page.title)
            
        except Exception as e:
            print(f"❌ Error occurred: {str(e)}")
        finally:
            browser.close()
        
if __name__ == "__main__":
    login_canvas()