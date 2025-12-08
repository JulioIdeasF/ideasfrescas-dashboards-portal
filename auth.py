import streamlit as st
import requests
from urllib.parse import urlencode, urlparse, parse_qs
from jose import jwt

def get_auth0_config():
    cfg = st.secrets["auth0"]
    return {
        "domain": cfg["domain"],
        "client_id": cfg["client_id"],
        "client_secret": cfg["client_secret"],
        "redirect_uri": cfg["redirect_uri"],
        "audience": cfg["audience"],
    }

def build_login_url():
    cfg = get_auth0_config()
    params = {
        "response_type": "code",
        "client_id": cfg["client_id"],
        "redirect_uri": cfg["redirect_uri"],
        "scope": "openid profile email",
        "audience": cfg["audience"],
    }
    return f"https://{cfg['domain']}/authorize?{urlencode(params)}"

def handle_callback():
    """Lee el parámetro ?code= de la URL y obtiene el token desde Auth0."""
    cfg = get_auth0_config()

    # Usar solo la nueva API: st.query_params
    code = st.query_params.get("code")

    if not code:
        return None

    token_url = f"https://{cfg['domain']}/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": cfg["client_id"],
        "client_secret": cfg["client_secret"],
        "code": code,
        "redirect_uri": cfg["redirect_uri"],
    }

    resp = requests.post(token_url, data=data)
    if resp.status_code != 200:
        st.error("Error intercambiando el código por token.")
        st.write(resp.text)
        return None

    tokens = resp.json()
    id_token = tokens.get("id_token")
    access_token = tokens.get("access_token")

    # Decodificar el id_token (por ahora sin validar firma, solo para pruebas)
    try:
        from jose import jwt
        decoded = jwt.get_unverified_claims(id_token)
    except Exception as e:
        st.error("Error decodificando el token.")
        st.write(str(e))
        return None

    user_info = {
        "email": decoded.get("email"),
        "name": decoded.get("name"),
        "sub": decoded.get("sub"),
        "raw_id_token": id_token,
        "access_token": access_token,
        "roles": decoded.get("dev-ajifaa3ovgdvp4ty.us.auth0.com/roles", []),
    }

    # Guardar en sesión
    st.session_state["user"] = user_info

    # Limpiar el parámetro ?code= de la URL usando solo la nueva API
    st.query_params.clear()

    return user_info
    

def get_current_user():
    """Devuelve el usuario desde session_state, si existe."""
    return st.session_state.get("user")

def logout_button():
    cfg = get_auth0_config()
    if st.button("Cerrar sesión"):
        st.session_state.pop("user", None)
        logout_url = (
            f"https://{cfg['domain']}/v2/logout?"
            + urlencode({"client_id": cfg["client_id"], "returnTo": cfg["redirect_uri"]})
        )
        st.markdown(f"[Click aquí para cerrar sesión]({logout_url})", unsafe_allow_html=True)
