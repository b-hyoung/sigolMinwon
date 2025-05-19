import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className="text-3xl text-red-600 font-bold p-4">
      ✅ Tailwind 적용됨!
    </div>
    </>
  )
}

export default App
