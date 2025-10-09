import React, { useState, useEffect } from 'react';
import './Gallery.css';

function Gallery() {
  const [galleryData, setGalleryData] = useState(null);
  const [selectedImage, setSelectedImage] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchGallery();
  }, []);

  const fetchGallery = async () => {
    try {
      const response = await fetch('/api/gallery');
      const data = await response.json();
      setGalleryData(data);
    } catch (error) {
      console.error('Error fetching gallery:', error);
    } finally {
      setLoading(false);
    }
  };

  const openLightbox = (image) => {
    setSelectedImage(image);
  };

  const closeLightbox = () => {
    setSelectedImage(null);
  };

  if (loading) {
    return <div className="spinner"></div>;
  }

  // Local images for gallery
  const localImages = [
    { id: 1, url: '/images/gallery-cafe-interior.webp', caption: 'Elegant Dining Room' },
    { id: 2, url: '/images/gallery-ribeye-steak.webp', caption: 'Signature Ribeye Steak' },
    { id: 3, url: '/images/gallery-special-event.webp', caption: 'Private Events' },
    { id: 4, url: '/images/home-cafe-fausse.webp', caption: 'Restaurant Exterior' }
  ];

  return (
    <div className="gallery-page">
      <div className="page-hero">
        <h1>Gallery</h1>
        <p>A Visual Journey Through Café Fausse</p>
      </div>

      <div className="container">
        <section className="gallery-section">
          <h2>Our Space</h2>
          <div className="gallery-grid">
            {localImages.map(image => (
              <div key={image.id} className="gallery-item" onClick={() => openLightbox(image)}>
                <img src={image.url} alt={image.caption} />
                <div className="gallery-overlay">
                  <p>{image.caption}</p>
                </div>
              </div>
            ))}
          </div>
        </section>

        {galleryData && galleryData.awards && (
          <section className="awards-section">
            <h2>Awards & Recognition</h2>
            <div className="awards-grid">
              {galleryData.awards.map((award, index) => (
                <div key={index} className="award-card">
                  <div className="award-icon">🏆</div>
                  <h3>{award.title}</h3>
                  <p className="award-year">{award.year}</p>
                  <p className="award-org">{award.organization}</p>
                </div>
              ))}
            </div>
          </section>
        )}

        <section className="reviews-section">
          <h2>Guest Reviews</h2>
          <div className="reviews-grid">
            <div className="review-card">
              <div className="review-stars">⭐⭐⭐⭐⭐</div>
              <p className="review-text">
                "Exceptional ambiance and unforgettable flavors. Café Fausse delivers 
                an extraordinary dining experience every time."
              </p>
              <p className="review-author">- Gourmet Review</p>
            </div>
            <div className="review-card">
              <div className="review-stars">⭐⭐⭐⭐⭐</div>
              <p className="review-text">
                "A must-visit restaurant for food enthusiasts. The attention to detail 
                and quality is unmatched in the DC area."
              </p>
              <p className="review-author">- The Daily Bite</p>
            </div>
          </div>
        </section>
      </div>

      {/* Lightbox */}
      {selectedImage && (
        <div className="lightbox" onClick={closeLightbox}>
          <div className="lightbox-content">
            <img src={selectedImage.url} alt={selectedImage.caption} />
            <p>{selectedImage.caption}</p>
            <button className="lightbox-close" onClick={closeLightbox}>×</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Gallery;