<template>
  <div class="feed-frame">
    <document-frame
      v-for="pdf in $data.pdfs"
      v-bind:key="pdf.fingerprint"
      v-bind:="pdf"
    ></document-frame>
  </div>
</template>

<script>
import DocumentFrame from './DocumentFrame.vue';

const DOCUMENT_CHUNK_SIZE = 12;

export default {
  data() {
    return {
      pdfs: [],
      pdfOffset: 0,
    };
  },
  methods: {
    enableInfiniteScroll() {
      window.onscroll = this.infiniteScroll;
    },
    disableInfiniteScroll() {
      window.onscroll = undefined;
    },
    infiniteScroll() {
      const bottomOfWindow = document.documentElement.scrollTop + window.innerHeight
        >= 0.8 * document.documentElement.offsetHeight;

      if (bottomOfWindow) {
        this.disableInfiniteScroll();
        this.fetchDocuments();
      }
    },
    fetchDocuments() {
      this.axios
        .get(`${process.env.VUE_APP_BASE_URL}/v1/pdfs`, {
          params: {
            size: DOCUMENT_CHUNK_SIZE,
            offset: this.$data.pdfOffset,
          },
        })
        .then((response) => {
          const newPdfs = response.data;
          const newPdfsCount = newPdfs ? newPdfs.length : 0;

          if (!newPdfsCount) {
            return;
          }

          this.$data.pdfOffset += newPdfsCount;
          this.$data.pdfs = this.$data.pdfs.concat(newPdfs);
          this.enableInfiniteScroll();
        });
    },
  },
  mounted() {
    this.enableInfiniteScroll();
    this.fetchDocuments();
  },

  name: 'TheDocumentFeed',
  components: {
    DocumentFrame,
  },
  props: {
    msg: String,
  },
};
</script>

<style scoped>
.feed-frame {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-content: space-around;
  justify-content: center;
  margin-left: 5%;
  margin-right: 5%;
}
</style>
