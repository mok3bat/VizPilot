from contextlib import contextmanager
from tableauserverclient import Server, PersonalAccessTokenAuth
from config_utils import get_config_value

@contextmanager
def tableau_connection():
    """Context manager for authenticated Tableau Server connection."""
    auth = PersonalAccessTokenAuth(
        token_name=get_config_value("TABLEAU_PERSONAL_ACCESS_TOKEN_NAME"),
        personal_access_token=get_config_value("TABLEAU_PERSONAL_ACCESS_TOKEN_SECRET"),
        site_id=get_config_value("TABLEAU_SITE_ID")
    )
    server = Server(get_config_value("TABLEAU_SERVER_URL"), use_server_version=True)

    try:
        server.auth.sign_in(auth)
        yield server
    finally:
        server.auth.sign_out()



def query_metadata(query=""):
    with tableau_connection() as server:
        workbooks, _ = server.workbooks.get()
        result = [f"Workbook: {wb.name}, Owner: {wb.owner_id}" for wb in workbooks]
        return "\n".join(result)



def get_tableau_metadata():
    with tableau_connection() as server:
        workbooks, _ = server.workbooks.get()
        results = []
        for wb in workbooks:
            print(f"📊 Found workbook: {wb.name}")
            results.append({
                "text": f"Workbook: {wb.name}, Project: {wb.project_name}",
                "source": wb.name
            })
        return results

