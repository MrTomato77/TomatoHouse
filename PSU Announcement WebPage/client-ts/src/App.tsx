import './App.css';
import AppRoutes from './config/routes';
import { AuthProvider } from "react-oidc-context";
import AppProvider from './AppProvider';
import { oidcConfig } from './config';

function App() {
  return (
    <AuthProvider{...oidcConfig}>
      <AppProvider>
        <AppRoutes />
      </AppProvider>      
    </AuthProvider>
  )
}

export default App;