function menutoogle(){
    const app = document.querySelector("#app_profile")
    const manage = document.querySelector(".manage_account_picture")
    app.classList.toggle('active')
    manage.classList.toggle('active')
}
function menu(){
    const data_base = document.querySelector(".data_base_aproved")
    const data_pie = document.querySelector(".data_base_pie")
    data_base.classList.toggle('active')
    data_pie.classList.toggle('active')
}
function submit(){ 
    document.submit.submit()
}
function show_me(){
    const urlme = document.querySelector(".urlme")
    const pusle = document.querySelector(".pulse_google_cloud")
    urlme.classList.toggle('show')
    pusle.classList.toggle('show')
}