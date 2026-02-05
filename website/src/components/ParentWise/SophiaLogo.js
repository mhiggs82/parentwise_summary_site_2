import React from 'react';

export default function SophiaLogo({ size = 120 }) {
    return (
        <div style={{
            width: size,
            height: size,
            borderRadius: '50%',
            background: 'var(--pw-purple)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            boxShadow: '0 0 30px var(--pw-purple-glow)',
            margin: '0 auto 24px'
        }}>
            <img
                src="/img/sophia-logo-white.svg"
                alt="Sophia Logo"
                style={{
                    width: size * 0.6,
                    height: size * 0.6,
                    objectFit: 'contain'
                }}
            />
        </div>
    );
}
