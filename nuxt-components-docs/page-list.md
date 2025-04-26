<!-- source: https://ui.nuxt.com/components/page-list --> # PageListPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/PageList.vue)

A vertical list layout for displaying content in a stacked format.

## Usage

The PageList component provides a flexible way to display content in a
vertical list layout. It's perfect for creating stacked lists of
[PageCard](/components/page-card) components or any other elements, with
optional dividers between items.

![benjamincanac](https://github.com/benjamincanac.png)

Benjamin Canac

benjamincanac

[](https://github.com/benjamincanac)

![smarroufin](https://github.com/smarroufin.png)

Sylvain Marroufin

smarroufin

[](https://github.com/smarroufin)

![atinux](https://github.com/atinux.png)

Sébastien Chopin

atinux

[](https://github.com/atinux)

![romhml](https://github.com/romhml.png)

Romain Hamel

romhml

[](https://github.com/romhml)

    
    
    <script setup lang="ts">
    const users = ref([
      {
        name: 'Benjamin Canac',
        description: 'benjamincanac',
        to: 'https://github.com/benjamincanac',
        target: '_blank',
        avatar: {
          src: 'https://github.com/benjamincanac.png',
          alt: 'benjamincanac'
        }
      },
      {
        name: 'Sylvain Marroufin',
        description: 'smarroufin',
        to: 'https://github.com/smarroufin',
        target: '_blank',
        avatar: {
          src: 'https://github.com/smarroufin.png',
          alt: 'smarroufin'
        }
      },
      {
        name: 'Sébastien Chopin',
        description: 'atinux',
        to: 'https://github.com/atinux',
        target: '_blank',
        avatar: {
          src: 'https://github.com/atinux.png',
          alt: 'atinux'
        }
      },
      {
        name: 'Romain Hamel',
        description: 'romhml',
        to: 'https://github.com/romhml',
        target: '_blank',
        avatar: {
          src: 'https://github.com/romhml.png',
          alt: 'romhml'
        }
      }
    ])
    </script>
    
    <template>
      <UPageList>
        <UPageCard
          v-for="(user, index) in users"
          :key="index"
          variant="ghost"
          :to="user.to"
          :target="user.target"
        >
          <template #body>
            <UUser :name="user.name" :description="user.description" :avatar="user.avatar" size="xl" class="relative" />
          </template>
        </UPageCard>
      </UPageList>
    </template>
    

Expand code

### Divide

Use the `divide` prop to add a divider between each child element.

![benjamincanac](https://github.com/benjamincanac.png)

Benjamin Canac

benjamincanac

[](https://github.com/benjamincanac)

![smarroufin](https://github.com/smarroufin.png)

Sylvain Marroufin

smarroufin

[](https://github.com/smarroufin)

![atinux](https://github.com/atinux.png)

Sébastien Chopin

atinux

[](https://github.com/atinux)

![romhml](https://github.com/romhml.png)

Romain Hamel

romhml

[](https://github.com/romhml)

    
    
    <script setup lang="ts">
    const users = ref([
      {
        name: 'Benjamin Canac',
        description: 'benjamincanac',
        to: 'https://github.com/benjamincanac',
        target: '_blank',
        avatar: {
          src: 'https://github.com/benjamincanac.png',
          alt: 'benjamincanac'
        }
      },
      {
        name: 'Sylvain Marroufin',
        description: 'smarroufin',
        to: 'https://github.com/smarroufin',
        target: '_blank',
        avatar: {
          src: 'https://github.com/smarroufin.png',
          alt: 'smarroufin'
        }
      },
      {
        name: 'Sébastien Chopin',
        description: 'atinux',
        to: 'https://github.com/atinux',
        target: '_blank',
        avatar: {
          src: 'https://github.com/atinux.png',
          alt: 'atinux'
        }
      },
      {
        name: 'Romain Hamel',
        description: 'romhml',
        to: 'https://github.com/romhml',
        target: '_blank',
        avatar: {
          src: 'https://github.com/romhml.png',
          alt: 'romhml'
        }
      }
    ])
    </script>
    
    <template>
      <UPageList divide>
        <UPageCard
          v-for="(user, index) in users"
          :key="index"
          variant="ghost"
          :to="user.to"
          :target="user.target"
        >
          <template #body>
            <UUser :name="user.name" :description="user.description" :avatar="user.avatar" size="xl" />
          </template>
        </UPageCard>
      </UPageList>
    </template>
    

Expand code

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`divide`| `false`| `boolean`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        pageList: {
          base: 'relative flex flex-col',
          variants: {
            divide: {
              true: '*:not-last:after:absolute *:not-last:after:inset-x-1 *:not-last:after:bottom-0 *:not-last:after:bg-border *:not-last:after:h-px'
            }
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          uiPro: {
            pageList: {
              base: 'relative flex flex-col',
              variants: {
                divide: {
                  true: '*:not-last:after:absolute *:not-last:after:inset-x-1 *:not-last:after:bottom-0 *:not-last:after:bg-border *:not-last:after:h-px'
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          uiPro: {
            pageList: {
              base: 'relative flex flex-col',
              variants: {
                divide: {
                  true: '*:not-last:after:absolute *:not-last:after:inset-x-1 *:not-last:after:bottom-0 *:not-last:after:bg-border *:not-last:after:h-px'
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[PageLinksA list of links to be displayed in the page.](/components/page-
links)[PageLogosA list of logos or images to display on your
pages.](/components/page-logos)

