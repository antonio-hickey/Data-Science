import React, { useState, useEffect } from 'react';
import logo from '../buffer.gif';
import '../App.css';

function App() {
  const [heading1, setHeading1] = useState('to close to call');
  useEffect(() => {
    fetch('/heading1').then(res => res.json()).then(data => {
      setHeading1(data.heading);
    });
  }, []);

  const [heading2, setHeading2] = useState('to close to call');
  useEffect(() => {
	fetch('/heading2').then(res => res.json()).then(data1 => {
	  setHeading2(data1.heading2);
	});
  }, []);

  const [heading3, setHeading3] = useState('to close to call');
  useEffect(() => {
  	fetch('/heading3').then(res => res.json()).then(data2 => {
  	  setHeading3(data2.heading3);
  	});
  }, []);

  const [f1c1, setf1c1] = useState('to close to call');
  useEffect(() => {
  	fetch('/f1c1').then(res => res.json()).then(data2 => {
  	  setf1c1(data2.f1c1);
  	});
  }, []);

  const [f1c2, setf1c2] = useState('to close to call');
  useEffect(() => {
  	fetch('/f1c2').then(res => res.json()).then(data2 => {
  	  setf1c2(data2.f1c2);
  	});
  }, []);

  const [f1c3, setf1c3] = useState('N/A');
  useEffect(() => {
  	fetch('/f1c3').then(res => res.json()).then(data2 => {
  	  setf1c3(data2.f1c3);
  	});
  }, []);

  const [f2c1, setf2c1] = useState('to close to call');
  useEffect(() => {
  	fetch('/f2c1').then(res => res.json()).then(data2 => {
  	  setf2c1(data2.f2c1);
  	});
  }, []);
  const [f2c2, setf2c2] = useState('to close to call');
  useEffect(() => {
  	fetch('/f2c2').then(res => res.json()).then(data2 => {
  	  setf2c2(data2.f2c2);
  	});
  }, []);
  const [f2c3, setf2c3] = useState('N/A');
  useEffect(() => {
  	fetch('/f2c3').then(res => res.json()).then(data2 => {
  	  setf2c3(data2.f2c3);
  	});
  }, []);

  const [f3c1, setf3c1] = useState('to close to call');
  useEffect(() => {
  	fetch('/f3c1').then(res => res.json()).then(data2 => {
  	  setf3c1(data2.f3c1);
  	});
  }, []);

  const [f3c2, setf3c2] = useState('to close to call');
  useEffect(() => {
  	fetch('/f3c2').then(res => res.json()).then(data2 => {
  	  setf3c2(data2.f3c2);
  	});
  }, []);

  const [f3c3, setf3c3] = useState('N/A');
  useEffect(() => {
  	fetch('/f3c3').then(res => res.json()).then(data2 => {
  	  setf3c3(data2.f3c3);
  	});
  }, []);
  const [f4c1, setf4c1] = useState('to close to call');
  useEffect(() => {
  	fetch('/f4c1').then(res => res.json()).then(data2 => {
  	  setf4c1(data2.f4c1);
  	});
  }, []);

  const [f4c2, setf4c2] = useState('to close to call');
  useEffect(() => {
  	fetch('/f4c2').then(res => res.json()).then(data2 => {
  	  setf4c2(data2.f4c2);
  	});
  }, []);

  const [f4c3, setf4c3] = useState('N/A');
  useEffect(() => {
  	fetch('/f4c3').then(res => res.json()).then(data2 => {
  	  setf4c3(data2.f4c3);
  	});
  }, []);

  const [f5c1, setf5c1] = useState('to close to call');
  useEffect(() => {
  	fetch('/f5c1').then(res => res.json()).then(data2 => {
  	  setf5c1(data2.f5c1);
  	});
  }, []);

  const [f5c2, setf5c2] = useState('to close to call');
  useEffect(() => {
  	fetch('/f5c2').then(res => res.json()).then(data2 => {
  	  setf5c2(data2.f5c2);
  	});
  }, []);

  const [f5c3, setf5c3] = useState('N/A');
  useEffect(() => {
  	fetch('/f5c3').then(res => res.json()).then(data2 => {
  	  setf5c3(data2.f5c3);
  	});
  }, []);

  return (
    <div className="Appski">
      <header className="App-header">
        <img src={logo} className="App-logo-1" alt="logo" />
        <div className="Tableski">
          <table>
		        <thead>
		        	<tr>
  						<th>{heading1}</th>
  						<th>{heading2}</th>
  						<th>{heading3}</th>
		        	</tr>
		        </thead>
		        <tbody>
		        	<tr>
                <td>{f1c1}</td>
		        		<td>{f1c2}</td>
		        		<td>{f1c3}</td>
		        	</tr>
		        	<tr>
		        		<td>{f2c1}</td>
		        		<td>{f2c2}</td>
		        		<td>{f2c3}</td>
		        	</tr>
		        	<tr>
		        		<td>{f3c1}</td>
		        		<td>{f3c2}</td>
		        		<td>{f3c3}</td>
		        	</tr>
		        	<tr>
		        		<td>{f4c1}</td>
		        		<td>{f4c2}</td>
		        		<td>{f4c3}</td>
		        	</tr>
		        	<tr>
		        		<td>{f5c1}</td>
		        		<td>{f5c2}</td>
		        		<td>{f5c3}</td>
		        	</tr>
		        </tbody>
	        </table>
        </div>
      </header>
    </div>
  );
}

export default App;
