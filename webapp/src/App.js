import './App.css';
import Container from '@mui/material/Container';
import { DataGrid } from '@mui/x-data-grid';

import getMovieList from './networkService';
import { CircularProgress } from '@mui/material';
import { useQuery } from 'react-query';



function App() {
  const columns = [
    { field: 'id', headerName: 'ID', width: 90 },
    {
      field: 'title',
      headerName: 'Title',
      width: 150,
    },
    {
      field: 'budget',
      headerName: 'Budget',
      width: 150,
    },
    {
      field: 'genres',
      headerName: 'Genres',
      width: 110,
    },
    {
      field: 'genres',
      headerName: 'Genres',
      width: 110,
    },
    {
      field: 'overview',
      headerName: 'Overview',
      width: 110,
    },
    {
      field: 'tagline',
      headerName: 'Tag line',
      width: 110,
    },
    {
      field: 'cast',
      headerName: 'Cast',
      width: 110,
    },
    {
      field: 'Director',
      headerName: 'director',
      width: 110,
    }
  ];

  const { data } = useQuery(["movie_list"],
    () => getMovieList()
  )

  if (data) {
    return (

      <div style={{ height: 700, width: '100%' }}>
        <DataGrid
          columns={columns}
          rows={data}
          pageSize={10}
          rowsPerPageOptions={[15]}
          checkboxSelection
          disableSelectionOnClick
        />
      </div>
    )
  } else {
    return <CircularProgress />
  };
}

export default App;
