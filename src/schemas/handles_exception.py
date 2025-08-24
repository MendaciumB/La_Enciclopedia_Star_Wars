import httpx

class RequestFailure(Exception): ...

class HTTPStatusFailure(Exception): ...

def get_handles_exception(session: httpx.Client, url: str) -> httpx.Response:
    """Handles exceptions for HTTP requests."""
    try:
        response = session.get(url)
        return response.raise_for_status()
    except httpx.RequestError as e:
        print(f"An error occurred while requesting {e.request.url!r}.")
        raise RequestFailure("The page is down") from e
    except httpx.HTTPStatusError as e:
        print(f"Error response {e.response.status_code} while requesting {e.request.url!r}.")
        raise HTTPStatusFailure("The url is wrong") from e



# if __name__ == "__main__":
#     url = "https://swapi.info/api/"
#     swapi_service: httpx.Client = httpx.Client()
#     get_handles_exception(swapi_service, url)