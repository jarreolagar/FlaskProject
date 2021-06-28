<template>
    <div>
        <center>
            <h1 class="titulo">Bienvenidos.</h1><br>
        </center>
        
        <div v-for="(entrada, index) in entradas" :key="index" class="textos">
            <h3>{{ entrada.titulo }}</h3>
            <p>{{ entrada.articulo }}</p>
            <p>{{ entrada.fecha }}</p>
            <br>
            <hr>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            entradas:[],
        }
    },
    methods:{
        getEntradas(){
            fetch('http://127.0.0.1:5000/leer_entrada', {
                method: "GET",
                headers: {
                    "Content-Type":"application/json"
                }
            })
            .then(resp => resp.json()) 
            .then(data => {
                this.entradas.push(...data)
            })
            .catch(error => {
                console.log(error)
            })    
        },
    },
    created(){
        this.getEntradas();
    },
};
</script>

<style>
.titulo{
    font-family: Arial, Helvetica, sans-serif;
    font-size: 60px;
    margin-top: 30px;
}

.textos{
    padding-left: 100px;
}
</style>
