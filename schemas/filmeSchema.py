from pydantic import BaseModel, Field
from typing import List, Optional


class Filme(BaseModel):
    id: int = Field(..., description="ID do filme")
    title: str = Field(..., description="Título do filme")
    overview: str = Field(..., description="Sinopse do filme")
    release_date: str = Field(..., description="Data de lançamento")
    adult: bool = Field(..., description="Indicador de conteúdo adulto")
    backdrop_path: Optional[str] = Field(None, description="Caminho da imagem de fundo")
    genre_ids: List[int] = Field(..., description="IDs dos gêneros")
    original_language: str = Field(..., description="Idioma original")
    original_title: str = Field(..., description="Título original")
    popularity: float = Field(..., description="Popularidade")
    poster_path: Optional[str] = Field(None, description="Caminho do pôster")
    video: bool = Field(..., description="Indicador de vídeo")
    vote_average: float = Field(..., description="Média de votos")
    vote_count: int = Field(..., description="Contagem de votos")
    comments: Optional[str] = Field(None, description="Comentário adicionado")


class FilmeUpdateParcial(BaseModel):
    comments: Optional[str] = Field(None, description="Comentário adicionado")


class FilmeId(BaseModel):
    filme_id: int = Field(..., description="ID do filme")


class FilmeList(BaseModel):
    filmes: List[Filme]
