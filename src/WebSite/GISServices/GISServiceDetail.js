import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { makeStyles } from '@material-ui/core/styles';
import axios from 'axios';
import { basewebURL } from '../../basewebURL';

const useStyles = makeStyles((theme) => ({
  container: {
    padding: '40px 20px',
    maxWidth: '1000px',
    margin: '0 auto',
  },
  serviceImage: {
    width: '100%',
    maxHeight: '400px',
    objectFit: 'cover',
    borderRadius: '8px',
    marginBottom: '30px',
  },
  serviceTitle: {
    fontSize: '2.2rem',
    fontWeight: 'bold',
    marginBottom: '15px',
    color: '#333',
  },
  serviceDescription: {
    fontSize: '1rem',
    color: '#555',
    lineHeight: '1.8',
    marginBottom: '30px',
  },
  section: {
    marginTop: '30px',
  },
  sectionTitle: {
    fontSize: '1.5rem',
    fontWeight: 'bold',
    marginBottom: '15px',
    color: '#333',
    borderBottom: '2px solid var(--themeColor)',
    paddingBottom: '10px',
  },
  listItem: {
    fontSize: '1rem',
    color: '#555',
    marginBottom: '10px',
    paddingLeft: '20px',
    position: 'relative',
    '&:before': {
      content: '"✓"',
      position: 'absolute',
      left: '0',
      color: 'var(--themeColor)',
      fontWeight: 'bold',
    },
  },
  backButton: {
    backgroundColor: 'var(--themeColor)',
    color: '#fff',
    padding: '10px 20px',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    fontSize: '0.95rem',
    marginBottom: '30px',
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
}));

const GISServiceDetail = ({ passMountInfo }) => {
  const classes = useStyles();
  const { id } = useParams();
  const [service, setService] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (passMountInfo) {
      passMountInfo(true);
    }

    const fetchService = async () => {
      try {
        setLoading(true);
        const response = await axios.get(`${basewebURL}/api/gis-services/${id}/`);
        setService(response.data);
        setError(null);
      } catch (err) {
        console.error('Error fetching GIS service:', err);
        setError('Failed to load this GIS service');
        setService(null);
      } finally {
        setLoading(false);
      }
    };

    fetchService();
  }, [id, passMountInfo]);

  const handleBackClick = () => {
    window.location.href = '/gis-services';
  };

  if (loading) {
    return <div className={classes.loadingContainer}>Loading service details...</div>;
  }

  if (error) {
    return (
      <div className={classes.container}>
        <button className={classes.backButton} onClick={handleBackClick}>
          ← Back to GIS Services
        </button>
        <div className={classes.errorContainer}>{error}</div>
      </div>
    );
  }

  if (!service) {
    return (
      <div className={classes.container}>
        <button className={classes.backButton} onClick={handleBackClick}>
          ← Back to GIS Services
        </button>
        <div className={classes.errorContainer}>Service not found</div>
      </div>
    );
  }

  return (
    <div className={classes.container}>
      <button className={classes.backButton} onClick={handleBackClick}>
        ← Back to GIS Services
      </button>

      {service.image && (
        <img src={service.image} alt={service.title} className={classes.serviceImage} />
      )}

      <h1 className={classes.serviceTitle}>{service.title}</h1>

      <p className={classes.serviceDescription}>{service.description}</p>

      {service.long_description && (
        <div className={classes.section}>
          <div className={classes.sectionTitle}>Overview</div>
          <p style={{ fontSize: '1rem', color: '#555', lineHeight: '1.8' }}>
            {service.long_description}
          </p>
        </div>
      )}

      {service.features && service.features.length > 0 && (
        <div className={classes.section}>
          <div className={classes.sectionTitle}>Key Features</div>
          {service.features.map((feature, idx) => (
            <div key={idx} className={classes.listItem}>
              {feature}
            </div>
          ))}
        </div>
      )}

      {service.benefits && service.benefits.length > 0 && (
        <div className={classes.section}>
          <div className={classes.sectionTitle}>Benefits</div>
          {service.benefits.map((benefit, idx) => (
            <div key={idx} className={classes.listItem}>
              {benefit}
            </div>
          ))}
        </div>
      )}

      {service.technologies && service.technologies.length > 0 && (
        <div className={classes.section}>
          <div className={classes.sectionTitle}>Technologies Used</div>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '10px' }}>
            {service.technologies.map((tech, idx) => (
              <span
                key={idx}
                style={{
                  backgroundColor: 'var(--themeColor)',
                  color: '#fff',
                  padding: '8px 15px',
                  borderRadius: '20px',
                  fontSize: '0.9rem',
                }}
              >
                {tech}
              </span>
            ))}
          </div>
        </div>
      )}

      {service.use_cases && service.use_cases.length > 0 && (
        <div className={classes.section}>
          <div className={classes.sectionTitle}>Use Cases</div>
          {service.use_cases.map((useCase, idx) => (
            <div key={idx} className={classes.listItem}>
              {useCase}
            </div>
          ))}
        </div>
      )}

      <div style={{ marginTop: '50px' }}>
        <button className={classes.backButton} onClick={handleBackClick}>
          ← Back to GIS Services
        </button>
      </div>
    </div>
  );
};

export default GISServiceDetail;
