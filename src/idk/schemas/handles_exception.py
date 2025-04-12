import httpx

def get_handles_exception(session: httpx.Client, url: str) -> httpx.Response | None:
    """Handles exceptions for HTTP requests."""
    try:
        response = session.get(url)
        return response.raise_for_status()
    except httpx.RequestError as exc:
        print(f"An error occurred while requesting {exc.request.url!r}.")
    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")



# if __name__ == "__main__":
#     url = "https://swapi.dev/api/peopl/"
#     print(get_exception_manager(url))