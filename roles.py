import streamlit as st

def show_dashboard_for_role(user):
    roles = user.get("roles", [])

    # Sidebar
    st.sidebar.title("Portal de Dashboards")
    st.sidebar.write(f"Usuario: {user.get('email')}")
    st.sidebar.write("Roles:")
    for r in roles:
        st.sidebar.write(f"- {r}")

    if not roles:
        st.warning("No tienes un rol asignado con dashboard. Contacta a soporte.")
        return

    # ---- Ruteo simple según rol ----
    # Admin general
    if "admin_ideasfrescas" in roles or any(r.startswith("admin") for r in roles):
        show_admin_panel()

    # Cliente REM
    elif "cliente_rem" in roles:
        show_rem_dashboard()

    # Cliente Tres Islas
    elif "cliente_tresislas" in roles:
        show_tres_islas_dashboard()

    # Si tiene rol pero no está mapeado a ningún dashboard
    else:
        st.warning("Tienes roles asignados pero ninguno está mapeado a un dashboard. Avísale a soporte.")

def show_admin_panel():
    st.title("Panel Admin · Ideas Frescas")
    st.write("Aquí irá el dashboard global para todos los proyectos.")
    st.info("Placeholder: luego conectamos tus dashboards reales.")

def show_rem_dashboard():
    st.title("Dashboard REM")
    st.write("Aquí irá el dashboard de REM (proyectos inmobiliarios).")
    st.info("Placeholder.")

def show_tres_islas_dashboard():
    st.title("Dashboard Tres Islas")
    st.write("Aquí irá el dashboard de fábrica + bar.")
    st.info("Placeholder.")
