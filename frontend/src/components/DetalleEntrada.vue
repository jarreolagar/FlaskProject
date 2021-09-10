<template>
    <div class="container mt-5">
      <h5>Nuevaentrada</h5>
      <h3>
        {{ entrada.titulo }}
      </h3>
      <p>{{ entrada.articulo }}</p>
      <p>{{ entrada.fecha }}</p>
      
    </div>  
    
</template>

<script>
export default {
  data() {
    return {
      entradas: {},
    };
  },
  props: {
    id: {
      type: [Number, String],
      required: true,
    },
  },
  methods: {
    getEntradasDetalles() {
      fetch(`http://127.0.0.1:5000/leer_entrada/${this.id}/`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          this.entrada = data
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getEntradasDetalles();
  },
};
</script>

<style>
</style>