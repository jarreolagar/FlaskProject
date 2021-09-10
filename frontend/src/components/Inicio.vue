<template>
  <div>
    <center>
      <h1 class="titulo">Bienvenidos.</h1>
      <br />
    </center>

    <div v-for="entrada in entradas" :key="entrada.id" class="textos">
      <h3>
        <router-link
        :to="{name:'DetalleEntrada', params:{id:entrada.id}}"
        >
        {{ entrada.titulo }}
        </router-link>
      </h3>
      <p>{{ entrada.id }}</p>
      <p>{{ entrada.articulo }}</p>
      <p>{{ entrada.fecha }}</p>


      <button type="button" class="btn btn-primary" 
      @click="eliminarEntradas">
          Eliminar
      </button>
      <button type="button" class="btn btn-primary"
      @click="editarEntradas">
        Editar
      </button>
      <br />
    <div>
    </div>
      <hr />
    </div>
    
  </div>
</template>

<script>
export default {
  data() {
    return {
      entradas: [],
    };
  },
  props: {
    id: {
      type: [Number, String],
      required: true,
    },
  },
  methods: {
    getEntradas() {
      fetch("http://127.0.0.1:5000/leer_entrada", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          this.entradas.push(...data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  eliminarEntradas(){
    fetch(`http://127.0.0.1:5000/eliminar_entrada/${this.id}/`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then(() => {
          this.$router.push({
            name:'Entradas'
          })
        })
        .catch((error) => {
          console.log(error);
        });
  },
 
created() {
    this.getEntradas();
  },
    
};
</script>

<style>
.titulo {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 60px;
  margin-top: 30px;
}

.textos {
  padding-left: 100px;
}
</style>
