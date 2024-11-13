import React from 'react';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import './Home.css';
import foto1 from '../assets/foto1.png';
import foto2 from '../assets/foto2.png';
import foto3 from '../assets/foto3.png';
import foto4 from '../assets/foto4.png';

const Home = () => {
  const images = [foto1, foto2, foto3, foto4];

  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,
    arrows: true,
    centerMode: true,
    centerPadding: '0',
    adaptiveHeight: true
  };

  return (
    <div className="home">
      <h1>Welcome to Recipe Management App</h1>
      <div className="carousel-container">
        <Slider {...settings}>
          {images.map((image, index) => (
            <div key={index} className="carousel-slide">
              <img src={image} alt={`foto${index + 1}`} className="carousel-image" />
            </div>
          ))}
        </Slider>
      </div>
    </div>
  );
};

export default Home;
