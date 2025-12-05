import streamlit as st
from auth import build_login_url, handle_callback, get_current_user, logout_button
from roles import show_dashboard_for_role

st.set_page_config(page_title="Portal de Dashboards - Ideas Frescas", page_icon="📊", layout="wide")

def main():
    st.markdown(
        """
        <style>
        .centered {
            text-align: center;
            margin-top: 80px;
        }
        .login-btn {
            font-size: 18px;
            padding: 0.75rem 1.5rem;
            border-radius: 999px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    user = get_current_user()

    # 1) Si ya viene un code en la URL
    if not user:
        user = handle_callback()

    if user:
        # Usuario autenticado
        st.sidebar.title("Portal de Dashboards")
        logout_button()
        show_dashboard_for_role(user)
    else:
        # Pantalla de login
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        st.title("Portal de Dashboards · Ideas Frescas")
        st.subheader("Acceso exclusivo para clientes y equipo interno.")
        st.write("Inicia sesión para ver tu dashboard personalizado.")

        login_url = build_login_url()
        st.markdown(f"[👉 Iniciar sesión con cuenta segura]({login_url})", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
