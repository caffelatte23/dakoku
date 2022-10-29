<script setup lang="ts">
import axios from "axios";
import dayjs from "dayjs";

// 出勤時
const onAttend = (): void => {
  alert("出勤しました。");
  axios.post(import.meta.env.VITE_API_ROOT, {
    userId: "1",
    time: dayjs().format("YYYY-MM-DD HH:mm"),
    IsAttend: true,
  });
};

// 退勤時
const onLeave = (): void => {
  alert("退勤しました。");
  axios.post(import.meta.env.VITE_API_ROOT, {
    userId: "1",
    time: dayjs().format("YYYY-MM-DD HH:mm"),
    IsAttend: true,
  });
};
</script>

<template>
  <div class="body">
    <span>現在のステータス: 勤務時間外</span>
    <div class="button-container">
      <button class="button" @click="onAttend">出勤</button>
      <button class="button" @click="onLeave">退勤</button>
    </div>
  </div>
</template>

<style scoped>
.button {
  padding: 10px 30px;
  background-color: rgb(0, 174, 255);
  color: white;
  border: none;
  border-radius: 20px;
}

.button-container {
  display: flex;
  justify-content: space-evenly;
  width: 300px;
}

.body {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 300px;
  text-align: center;
}
</style>
