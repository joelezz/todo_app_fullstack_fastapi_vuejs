<template>
  <div class="container">
    <h1>📝 My Todo List</h1>

    <form @submit.prevent="addTask">
      <input v-model="newTask" placeholder="Enter a new task" />
      <button type="submit">Add Task</button>
    </form>

    <ul>
      <li v-for="task in tasks" :key="task.id">
        {{ task.description }} - 
        <span v-if="task.is_done">✅ Done</span>
        <button v-else @click="markDone(task.id)">Mark as done</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const tasks = ref([]);
const newTask = ref("");

const fetchTasks = async () => {
  const res = await fetch("http://127.0.0.1:8000/tasks");
  tasks.value = await res.json();
};

const addTask = async () => {
  if (!newTask.value.trim()) return;
  await fetch("http://127.0.0.1:8000/tasks", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ description: newTask.value }),
  });
  newTask.value = "";
  fetchTasks();
};

const markDone = async (id) => {
  await fetch(`http://127.0.0.1:8000/tasks/${id}/done`, {
    method: "PUT",
  });
  fetchTasks();
};

onMounted(fetchTasks);
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: auto;
  padding: 20px;
}
input {
  padding: 8px;
  margin-right: 10px;
}
button {
  padding: 8px 12px;
}
li {
  margin: 10px 0;
}
</style>
