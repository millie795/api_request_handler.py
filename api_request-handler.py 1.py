import requests

def get_user_data():
    url = "https://jsonplaceholder.typicode.com/users/1"

    try:
        print("Connecting to the API...")

        response = requests.get(url, timeout=10)

        # Check if the request was successful
        response.raise_for_status()

        # Convert the response to JSON
        data = response.json()

        # Check if the response contains valid information
        if not isinstance(data, dict) or "name" not in data:
            print("Error: The API returned an invalid response.")
            return

        # Display the user information
        print("\nAPI Request Successful!")
        print("-----------------------")
        print("Name:", data["name"])
        print("Email:", data.get("email", "Not available"))
        print("City:", data.get("address", {}).get("city", "Not available"))

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Error: Connection failed. Check your internet.")

    except requests.exceptions.HTTPError:
        print("Error: The server returned an unsuccessful response.")

    except ValueError:
        print("Error: The API returned invalid JSON data.")

    except requests.exceptions.RequestException:
        print("Error: Something went wrong with the API request.")


if __name__ == "__main__":
    get_user_data()