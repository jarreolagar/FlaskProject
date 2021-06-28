<template>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div id="desde1998">
        <router-link class="navbar-brand" to="/">desde1998</router-link>
    </div>
  
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav ms-auto">
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/">Inicio</router-link>
      </li>
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/leer_entrada">Entradas</router-link>
      </li>
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/escribeme">Sobre mi</router-link>
      </li>
    </ul>
  </div>
</nav>
</template>

<script>
export default {};
</script>

<style>
#desde1998{
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    margin-left: 50px;
}

.navbar-brand{
    font-size: 35px;
}

.nav-item{
    margin-right: 40px;
}
</style>

