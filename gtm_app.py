import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Simulador GTM Perú: AquaLevel", page_icon="💧", layout="wide")

st.title("💧 Simulador Estratégico Go-to-Market: AquaLevel Perú")
st.markdown("### Objetivo: Lograr el 'Product-Market Fit' en el mercado peruano")

# --- PANEL DE CONTROL (6 PREGUNTAS GTM) ---
st.sidebar.header("🕹️ Parámetros del Simulador")

# Opción por defecto para obligar a la selección
default_opt = "--- Selecciona una estrategia ---"

quien = st.sidebar.selectbox("1. ¿QUIÉN? (Audiencia)", 
    [default_opt, "Estudiantes Gen Z (Universidades)", "Amas de Casa", "Ejecutivos de San Isidro/Miraflores"])

que = st.sidebar.selectbox("2. ¿QUÉ? (Producto)", 
    [default_opt, "Agua Gamificada (QR + Avatar)", "Agua Mineral Económica", "Agua Premium en Vidrio"])

porque = st.sidebar.selectbox("3. ¿POR QUÉ? (Diferenciador)", 
    [default_opt, "Estatus y Diversión Digital", "Precio más bajo del mercado", "Exclusividad y Pureza"])

donde = st.sidebar.selectbox("4. ¿DÓNDE? (Canal)", 
    [default_opt, "Campus y Máquinas Inteligentes", "Supermercados y Mercados", "Restaurantes de Lujo"])

como = st.sidebar.selectbox("5. ¿CÓMO? (Promoción)", 
    [default_opt, "Retos TikTok y eventos en Campus", "Cupones y ofertas 2x1", "Publicidad en diarios de negocios"])

cuando = st.sidebar.selectbox("6. ¿CUÁNDO? (Timing)", 
    [default_opt, "Inicio de Ciclo Universitario (Marzo)", "Verano (Enero/Febrero)", "Campaña Navideña"])

# --- LÓGICA DE CÁLCULO ESTRATÉGICO ---
def calcular_simulacion():
    score = 0
    
    # El "Golden Path" (100% Alineación)
    if quien == "Estudiantes Gen Z (Universidades)":
        if que == "Agua Gamificada (QR + Avatar)": score += 20
        if porque == "Estatus y Diversión Digital": score += 15
        if donde == "Campus y Máquinas Inteligentes": score += 20
        if como == "Retos TikTok y eventos en Campus": score += 25
        if cuando == "Inicio de Ciclo Universitario (Marzo)": score += 20
    
    # Ruta de consumo masivo coherente
    elif quien == "Amas de Casa" and porque == "Precio más bajo del mercado" and donde == "Supermercados y Mercados":
        score = 70
        if cuando == "Verano (Enero/Febrero)": score += 10
        if que == "Agua Mineral Económica": score += 10
        
    score = max(5, min(100, score))
    
    # Métricas en Soles (S/)
    cac = max(1.50, 15.0 - (score * 0.135))
    
    if score == 100:
        cltv = 150.0  
    elif score >= 80:
        cltv = 80.0   
    elif score >= 50:
        cltv = 25.0   
    else:
        cltv = 3.50   
        
    roi = (cltv - cac) / cac
    return score, cac, cltv, roi

# --- CONTROL DE LANZAMIENTO ---
# Verificamos que no existan opciones por defecto seleccionadas
if st.sidebar.button("🚀 LANZAR AL MERCADO"):
    opciones = [quien, que, porque, donde, como, cuando]
    
    if default_opt in opciones:
        st.error("⚠️ **Error:** Por favor, selecciona una opción válida en todas las preguntas del GTM antes de lanzar.")
    else:
        with st.spinner("Analizando la respuesta del consumidor peruano..."):
            time.sleep(1.2)
        
        gtm_score, cac, cltv, roi = calcular_simulacion()

        # --- DASHBOARD DE RESULTADOS ---
        st.header("📊 Métricas de Desempeño (Cifras en Soles)")
        
        c1, c2, c3, c4 = st.columns(4)
        
        with c1:
            st.metric("GTM Alignment Score", f"{gtm_score}%")
            st.caption("Coherencia de la mezcla estratégica.")
            
        with c2:
            st.metric("CAC", f"S/ {cac:.2f}")
            st.caption("Costo de captar un cliente.")
            
        with c3:
            st.metric("CLTV", f"S/ {cltv:.2f}")
            st.caption("Valor del cliente en el tiempo.")
            
        with c4:
            st.metric("ROI", f"{roi:.1f}x")
            st.caption("Retorno de inversión por cliente.")

        # Feedback y Efectos visuales
        st.markdown("---")
        if gtm_score == 100:
            st.success("🏆 **¡ALINEACIÓN PERFECTA!** Has descifrado el mercado. AquaLevel es el nuevo estándar para los universitarios en Perú.")
            st.balloons() 
        elif gtm_score >= 80:
            st.success("✅ **Gran Trabajo.** Tu estrategia es muy sólida y rentable.")
        elif gtm_score >= 50:
            st.warning("⚠️ **Estrategia Aceptable.** Estás operando, pero el CAC es alto.")
        else:
            st.error("📉 **Fracaso Estratégico.** El negocio no es sostenible con estas decisiones.")

# --- LEYENDA Y EDUCACIÓN ---
with st.expander("📚 Glosario para Estudiantes de Administración"):
    st.write("""
    - **GTM Alignment Score:** Mide la sinergia entre las 6 preguntas.
    - **CAC (Customer Acquisition Cost):** ¿Cuánto nos costó en marketing atraer a este cliente?
    - **CLTV (Customer Lifetime Value):** ¿Cuántos Soles dejará el cliente en la empresa durante toda su vida útil?
    - **ROI (Return on Investment):** Eficiencia financiera de la estrategia.
    """)