import './App.css';
import { useQuery, gql } from '@apollo/client';

const GET_TEMPERATURE = gql`
  query {
    currentTemperature {
      timestamp
      value
    }
  }
`;

function DisplayTemperature() {
  const { loading, error, data } = useQuery(GET_TEMPERATURE);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error : {error.message}</p>;

  // return data.locations.map(({ id, name, description, photo }) => (
  return (
    <div>
      <h3>{data.currentTemperature.timestamp}</h3>
      <h3>{data.currentTemperature.value}</h3>
    </div>
  );
}
export default function App() {
  return (
    <div>
      <h2>My first Apollo app 🚀</h2>
      <br />
      <DisplayTemperature/>
    </div>
  );
}