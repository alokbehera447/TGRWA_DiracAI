import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import axios from 'axios';
import { basewebURL } from '../../basewebURL';

const useStyles = makeStyles((theme) => ({
  container: {
    padding: '40px 20px',
    maxWidth: '1200px',
    margin: '0 auto',
  },
  title: {
    fontSize: '2.5rem',
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: '40px',
    color: '#333',
  },
  servicesGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))',
    gap: '30px',
    marginTop: '30px',
  },
  serviceCard: {
    backgroundColor: '#fff',
    borderRadius: '8px',
    boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
    padding: '20px',
    transition: 'transform 0.3s, box-shadow 0.3s',
    '&:hover': {
      transform: 'translateY(-5px)',
      boxShadow: '0 4px 16px rgba(0,0,0,0.15)',
    },
  },
  serviceImage: {
    width: '100%',
    height: '200px',
    objectFit: 'cover',
    borderRadius: '4px',
    marginBottom: '15px',
  },
  serviceTitle: {
    fontSize: '1.3rem',
    fontWeight: 'bold',
    marginBottom: '10px',
    color: '#333',
  },
  serviceDescription: {
    fontSize: '0.95rem',
    color: '#666',
    marginBottom: '15px',
    lineHeight: '1.5',
  },
  viewMoreButton: {
    backgroundColor: 'var(--themeColor)',
    color: '#fff',
    padding: '10px 15px',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    fontSize: '0.9rem',
    transition: 'background-color 0.3s',
    '&:hover': {
      backgroundColor: 'var(--themeDarkerColor)',
    },
  },
  loadingContainer: {
    textAlign: 'center',
    padding: '40px',
    fontSize: '1.1rem',
    color: '#666',
  },
  errorContainer: {
    textAlign: 'center',
    padding: '40px',
    fontSize: '1.1rem',
    color: '#d32f2f',
  },
  noServicesContainer: {
    textAlign: 'center',
    padding: '40px',
    fontSize: '1.1rem',
    color: '#999',
  },
}));

const GISServices = ({ passMountInfo }) => {
  const classes = useStyles();
  const [services, setServices] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (passMountInfo) {
      passMountInfo(true);
    }

    const fetchGISServices = async () => {
      try {
        setLoading(true);
        const response = await axios.get(`${basewebURL}/api/gis-services/`);
        setServices(response.data);
        setError(null);
      } catch (err) {
        console.error('Error fetching GIS services:', err);
        setError('Failed to load GIS services');
        setServices([]);
      } finally {
        setLoading(false);
      }
    };

    fetchGISServices();
  }, [passMountInfo]);

  if (loading) {
    return <div className={classes.loadingContainer}>Loading GIS Services...</div>;
  }

  if (error) {
    return <div className={classes.errorContainer}>{error}</div>;
  }

  if (!services || services.length === 0) {
    return <div className={classes.noServicesContainer}>No GIS services available at the moment.</div>;
  }

  return (
    <div className={classes.container}>
      <h1 className={classes.title}>GIS Services & Solutions</h1>

      <div className={classes.servicesGrid}>
        {services.map((service) => (
          <div key={service.id || service.slug} className={classes.serviceCard}>
            {service.image && (
              <img src={service.image} alt={service.title} className={classes.serviceImage} />
            )}
            <h3 className={classes.serviceTitle}>{service.title}</h3>
            <p className={classes.serviceDescription}>{service.description}</p>
            {service.features && service.features.length > 0 && (
              <div style={{ marginBottom: '15px' }}>
                <strong>Key Features:</strong>
                <ul style={{ paddingLeft: '20px', marginTop: '8px' }}>
                  {service.features.slice(0, 3).map((feature, idx) => (
                    <li key={idx} style={{ fontSize: '0.85rem', color: '#555' }}>
                      {feature}
                    </li>
                  ))}
                </ul>
              </div>
            )}
            <button 
              className={classes.viewMoreButton}
              onClick={() => window.location.href = `/gis-services/${service.slug || service.id}`}
            >
              View Details
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default GISServices;
