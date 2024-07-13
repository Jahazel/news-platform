import { BrowserRouter, Routes, Route } from "react-router-dom";
import Signup from "./auth/Signup";
import Login from "./auth/Login";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/register" element={<Signup />}></Route>
          <Route path="/login" element={<Login />}></Route>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
