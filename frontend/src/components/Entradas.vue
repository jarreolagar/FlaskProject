<template>
    <div class="container mt-4">
        <form @submit.prevent="postEntradas">
            <input 
            type="text"
            class="form-control"
            placeholder="Ingresa un título"
            v-model="titulo">
            <br>

            <textarea rows="10"
            class="form-control"
            placeholder="Ingresa el texto de tu articulo"
            v-model="articulo">
            </textarea>
            <button class="btn btn-success mt-4">Agregar entrada</button>
        </form>
    </div>
</template>

<script>
export default {
    data(){
        return{
            titulo:null,
            articulo:null,
            fecha:null
        }
    },
    methods:{
        postEntradas(){
            if(!this.titulo || !this.articulo){
                this.error = "Llena todos los campos!"
                alert(this.error);
            }else{
                fetch('http://127.0.0.1:5000/agregar_entrada', {
                method: "POST",
                headers: {
                    "Content-Type":"application/json"
                },
                body: JSON.stringify({titulo:this.titulo, articulo:this.articulo})
            })
            .then(resp => resp.json()) 
            .then(() => {
                this.$router.push({
                    name:'Inicio'
                })
            })
            .catch(error => {
                console.log(error)
            })    
        }
    }} 
};
</script>