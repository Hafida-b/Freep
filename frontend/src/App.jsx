import { AuthProvider } from "./auth";
import Login from "./login";

function App() {
  return (
    <AuthProvider>
      <Login />
    </AuthProvider>
  );
}

export default App;
