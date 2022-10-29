<script setup lang="ts">
import axios from "axios";
import dayjs from "dayjs";
import { onMounted, ref } from "vue";

type status = "NOT_WORKING" | "WORKING";

interface workingStatus {
  userId: string;
  date: string;
  startTime: string;
  endTime: string;
  status: status;
}

const currentStatus = ref<workingStatus>({
  userId: "1",
  date: dayjs().format("YYYY-MM-DD"),
  startTime: "",
  endTime: "",
  status: "NOT_WORKING",
});

const Status: { NOT_WORKING: string; WORKING: string } = {
  NOT_WORKING: "勤務時間外",
  WORKING: "勤務中",
};

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
    IsAttend: false,
  });
};

const refreshStatus = (): void => {
  axios
    .get(import.meta.env.VITE_API_ROOT, {
      params: {
        userId: "1",
        date: dayjs().format("YYYY-MM-DD"),
      },
    })
    .then((res) => {
      currentStatus.value = res.data;
    });
};

onMounted((): void => refreshStatus());
</script>

<template>
  <div class="body">
    <span>現在のステータス: {{ Status[currentStatus.status] }}</span>
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
