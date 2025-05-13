
import streamlit as st
import pandas as pd

# Multilinguagem
LANGUAGES = {
    "Português": {
        "app_title": "Backlog Digital Brazil",
        "add_entry": "Adicionar Entrega",
        "export_data": "Exportar Dados",
        "client": "Cliente / Projeto",
        "solution": "Tipo de Solução",
        "stage": "Etapa Atual",
        "status": "Status",
        "internal": "Responsável Interno",
        "external": "Responsável no Cliente",
        "start_date": "Data de Início",
        "end_date": "Data Estimada de Entrega",
        "urgency": "Urgência",
        "macrolob": "Macrolob",
        "microlob": "Microlob",
        "seller": "Nome do Vendedor",
        "state": "Estado",
        "license": "Tipo de Licença",
        "sale_type": "Tipo de Venda",
        "contract_link": "Link do Contrato",
        "notes": "Observações",
        "summary": "Copiar Resumo",
        "send_email": "Simular Envio por Email"
    },
    "English": {
        "app_title": "Backlog Digital Brazil",
        "add_entry": "Add Entry",
        "export_data": "Export Data",
        "client": "Client / Project",
        "solution": "Solution Type",
        "stage": "Current Stage",
        "status": "Status",
        "internal": "Internal Responsible",
        "external": "Client Contact",
        "start_date": "Start Date",
        "end_date": "Estimated Delivery",
        "urgency": "Urgency",
        "macrolob": "Macrolob",
        "microlob": "Microlob",
        "seller": "Salesperson",
        "state": "State",
        "license": "License Type",
        "sale_type": "Sale Type",
        "contract_link": "Contract Link",
        "notes": "Notes",
        "summary": "Copy Summary",
        "send_email": "Simulate Email"
    },
    "Español": {
        "app_title": "Backlog Digital Brazil",
        "add_entry": "Agregar Entrega",
        "export_data": "Exportar Datos",
        "client": "Cliente / Proyecto",
        "solution": "Tipo de Solución",
        "stage": "Etapa Actual",
        "status": "Estado",
        "internal": "Responsable Interno",
        "external": "Contacto del Cliente",
        "start_date": "Fecha de Inicio",
        "end_date": "Entrega Estimada",
        "urgency": "Urgencia",
        "macrolob": "Macrolob",
        "microlob": "Microlob",
        "seller": "Vendedor",
        "state": "Estado",
        "license": "Tipo de Licencia",
        "sale_type": "Tipo de Venta",
        "contract_link": "Enlace del Contrato",
        "notes": "Observaciones",
        "summary": "Copiar Resumen",
        "send_email": "Simular Envío de Email"
    }
}

# Escolher idioma
language = st.sidebar.selectbox("Idioma / Language / Idioma", list(LANGUAGES.keys()))
L = LANGUAGES[language]

st.title(L["app_title"])

if "data" not in st.session_state:
    st.session_state["data"] = []

with st.form("add_form"):
    st.subheader(L["add_entry"])
    col1, col2 = st.columns(2)
    client = col1.text_input(L["client"])
    solution = col2.text_input(L["solution"])
    stage = col1.text_input(L["stage"])
    status = col2.selectbox(L["status"], ["Em andamento", "Pausado", "Concluído"])
    internal = col1.text_input(L["internal"])
    external = col2.text_input(L["external"])
    start_date = col1.date_input(L["start_date"])
    end_date = col2.date_input(L["end_date"])
    urgency = col1.selectbox(L["urgency"], ["Baixa", "Média", "Alta"])
    macrolob = col2.text_input(L["macrolob"])
    microlob = col1.text_input(L["microlob"])
    seller = col2.text_input(L["seller"])
    state = col1.text_input(L["state"])
    license_type = col2.text_input(L["license"])
    sale_type = col1.selectbox(L["sale_type"], ["New", "Renew", "Upgrade"])
    contract_link = col2.text_input(L["contract_link"])
    notes = st.text_area(L["notes"])

    submitted = st.form_submit_button("Salvar")
    if submitted:
        st.session_state["data"].append({
            "Cliente": client, "Solução": solution, "Etapa": stage, "Status": status,
            "Responsável Interno": internal, "Responsável Cliente": external,
            "Data Início": start_date, "Data Entrega": end_date,
            "Urgência": urgency, "Macrolob": macrolob, "Microlob": microlob,
            "Vendedor": seller, "Estado": state, "Licença": license_type,
            "Tipo de Venda": sale_type, "Contrato": contract_link, "Observações": notes
        })
        st.success("Projeto adicionado!")

if st.session_state["data"]:
    df = pd.DataFrame(st.session_state["data"])
    st.subheader("Backlog")
    st.dataframe(df)

    st.download_button(L["export_data"], df.to_csv(index=False), "backlog.csv")

