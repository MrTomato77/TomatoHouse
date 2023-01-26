import { CircleLoader } from 'react-spinners';
import './loading-screen.css';

const LoadingScreen = ({text} : {text:string}) => {
  return (
    <div className="loading-spinner-container">
      <CircleLoader color="#2980b9" size={150} />
      <div className="loading-text">{text}</div>
    </div>
  );
}

export default LoadingScreen;