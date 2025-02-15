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
            
            # FILL USERNAME AND PASSWORD
            page.fill("#username", username)
            page.fill("#password", password)
            page.click("text=LOG IN")
            
            page.wait_for_load_state('networkidle')
            
            print("✅ logged in successfully", page.title)
            
        except Exception as e:
            print(f"❌ Error occurred: {str(e)}")
        finally:
            browser.close()
        
if __name__ == "__main__":
    login_canvas()