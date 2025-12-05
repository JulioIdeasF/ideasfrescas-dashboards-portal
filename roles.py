import streamlit as st

def show_dashboard_for_role(user):
    roles = user.get("roles", [])

    st.sidebar.write(f"Usuario: {user.get('email')}")
    st.sidebar.write("Roles:")
    for r in roles:
        st.sidebar.write(f"- {r}")

    # Ejemplo de ruteo según roles
    if "admin" in roles:
        show_admin_panel()
    elif "cliente_rem" in roles:
        show_rem_dashboard()
    elif "cliente_tresislas" in roles:
        show_tres_islas_dashboard()
    else:
        st.warning("No tienes un rol asignado con dashboard. Contacta a soporte.")

def show_admin_panel():
    st.title("Panel Admin Ideas Frescas")
    st.write("Aquí podrás ver un resumen de todos los clientes, métricas globales, etc.")
    st.info("Aquí luego conectamos tus dashboards reales de admin.")

def show_rem_dashboard():
    st.title("Dashboard REM")
    st.write("Aquí irá el dashboard de REM (Mazatlán, lotes, etc.).")
    st.info("Por ahora es un placeholder para que pruebes la autenticación.")

def show_tres_islas_dashboard():
    st.title("Dashboard Tres Islas")
    st.write("Aquí irá el dashboard de Tres Islas (fábrica + bar).")
    st.info("Placeholder para pruebas.")
