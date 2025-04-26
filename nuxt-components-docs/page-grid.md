<!-- source: https://ui.nuxt.com/components/page-grid --> # PageGridPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/PageGrid.vue)

A responsive grid system for displaying content in a flexible layout.

## Usage

The PageGrid component provides a responsive grid layout for displaying
[PageCard](/components/page-card) components or any other elements,
automatically adjusting from 1 to 3 columns based on screen size.

Icons

Nuxt UI integrates with Nuxt Icon to access over 200,000+ icons from Iconify.

[](/getting-started/icons)

Fonts

Nuxt UI integrates with Nuxt Fonts to provide plug-and-play font optimization.

[](/getting-started/fonts)

Color Mode

Nuxt UI integrates with Nuxt Color Mode to switch between light and dark.

[](/getting-started/color-mode)

    
    
    <script setup lang="ts">
    const cards = ref([
      {
        title: 'Icons',
        description: 'Nuxt UI integrates with Nuxt Icon to access over 200,000+ icons from Iconify.',
        icon: 'i-lucide-smile',
        to: '/getting-started/icons'
      },
      {
        title: 'Fonts',
        description: 'Nuxt UI integrates with Nuxt Fonts to provide plug-and-play font optimization.',
        icon: 'i-lucide-a-large-small',
        to: '/getting-started/fonts'
      },
      {
        title: 'Color Mode',
        description: 'Nuxt UI integrates with Nuxt Color Mode to switch between light and dark.',
        icon: 'i-lucide-sun-moon',
        to: '/getting-started/color-mode'
      }
    ])
    </script>
    
    <template>
      <UPageGrid>
        <UPageCard
          v-for="(card, index) in cards"
          :key="index"
          v-bind="card"
        />
      </UPageGrid>
    </template>
    

You can also use it to display a list of cards in a bento style layout by
using `col-span-*` and `row-span-*` utility classes.

Theme

Learn how to customize Nuxt UI components using Tailwind CSS v4.

![Theme](https://ui2.nuxt.com/illustrations/color-palette-
light.svg)![Theme](https://ui2.nuxt.com/illustrations/color-palette-dark.svg)

[](/getting-started/theme)

Fonts

Nuxt UI integrates with Nuxt Fonts to provide plug-and-play font optimization.

[](/getting-started/fonts)

Color Mode

Nuxt UI integrates with Nuxt Color Mode to switch between light and dark.

[](/getting-started/color-mode)

Icons

Nuxt UI integrates with Nuxt Icon to access over 200,000+ icons from Iconify.

![Icons](https://ui2.nuxt.com/illustrations/icon-library-
light.svg)![Icons](https://ui2.nuxt.com/illustrations/icon-library-dark.svg)

[](/getting-started/icons)

    
    
    <script setup lang="ts">
    const cards = ref([
      {
        title: 'Theme',
        description: 'Learn how to customize Nuxt UI components using Tailwind CSS v4.',
        icon: 'i-lucide-swatch-book',
        to: '/getting-started/theme',
        class: 'lg:col-span-2',
        image: {
          path: 'https://ui2.nuxt.com/illustrations/color-palette',
          width: 363,
          height: 152
        },
        orientation: 'horizontal' as const
      },
      {
        title: 'Fonts',
        description: 'Nuxt UI integrates with Nuxt Fonts to provide plug-and-play font optimization.',
        icon: 'i-lucide-a-large-small',
        to: '/getting-started/fonts',
        variant: 'soft' as const
      },
      {
        title: 'Color Mode',
        description: 'Nuxt UI integrates with Nuxt Color Mode to switch between light and dark.',
        icon: 'i-lucide-sun-moon',
        to: '/getting-started/color-mode',
        variant: 'soft' as const
      },
      {
        title: 'Icons',
        description: 'Nuxt UI integrates with Nuxt Icon to access over 200,000+ icons from Iconify.',
        icon: 'i-lucide-smile',
        to: '/getting-started/icons',
        image: {
          path: 'https://ui2.nuxt.com/illustrations/icon-library',
          width: 362,
          height: 184
        },
        class: 'lg:col-span-2',
        orientation: 'horizontal' as const,
        reverse: true
      }
    ])
    </script>
    
    <template>
      <UPageGrid>
        <UPageCard
          v-for="(card, index) in cards"
          :key="index"
          v-bind="card"
        >
          <UColorModeImage
            v-if="card.image"
            :light="`${card.image.path}-light.svg`"
            :dark="`${card.image.path}-dark.svg`"
            :width="card.image.width"
            :height="card.image.height"
            :alt="card.title"
            loading="lazy"
            class="w-full"
          />
        </UPageCard>
      </UPageGrid>
    </template>
    

Expand code

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        pageGrid: {
          base: 'relative grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8'
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
            pageGrid: {
              base: 'relative grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8'
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
            pageGrid: {
              base: 'relative grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8'
            }
          }
        })
      ]
    })
    

Expand code

[PageFeatureA component to showcase key features of your
application.](/components/page-feature)[PageHeaderA responsive header for your
pages.](/components/page-header)

