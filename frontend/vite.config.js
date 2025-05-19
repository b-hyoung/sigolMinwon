import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  server: {
    host: '0.0.0.0', // ✅ 컨테이너 외부 접속 허용
    port: 5173
  },
  plugins: [react()]
})
